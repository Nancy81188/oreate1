    def save_journal_voucher(self,item,lines,user_id,entry_id=None):
        date=str(item.get("entry_date") or "").strip(); self._assert_period_open(date)
        description=str(item.get("description") or "").strip() or f"Journal Voucher {str(item.get('entry_number') or '').strip() or 'Entry'}"
        currency=str(item.get("currency") or "USD").upper()
        if not date or currency not in ("USD","EUR","LBP","AED"): raise ValueError("Enter voucher date, description, and currency")
        if not isinstance(lines,list) or len(lines)<2: raise ValueError("Journal Voucher requires at least two lines")
        normalized=[]; total_debit=Decimal("0"); total_credit=Decimal("0")
        voucher_type=str(item.get("voucher_type") or "01").strip()[:2] or "01"
        for index,line in enumerate(lines,1):
            code=str(line.get("account_code") or "").split(" - ",1)[0].strip(); extra=self._voucher_line_amounts(line,currency,date,index)
            if extra: debit,credit=extra["debit"],extra["credit"]
            else:
                try: debit=Decimal(str(line.get("debit") or 0)); credit=Decimal(str(line.get("credit") or 0))
                except Exception as exc: raise ValueError(f"Line {index}: Debit and Credit must be numbers") from exc
            if not code or min(debit,credit)<0 or (debit>0 and credit>0) or (debit==0 and credit==0): raise ValueError(f"Line {index}: choose an account and enter either Debit or Credit")
            normalized.append((code,str(line.get("description") or "").strip(),debit,credit,extra,line)); total_debit+=debit; total_credit+=credit
        if abs(total_debit-total_credit)>=Decimal("0.005"): raise ValueError(f"Journal Voucher is unbalanced. Debit {total_debit}; Credit {total_credit}; Remaining {abs(total_debit-total_credit):,.2f}")
        with self.connect() as db:
            branch_id=self._branch_id(db,item)
            if entry_id:
                existing=db.execute("SELECT * FROM journal_entries WHERE id=? AND source_type='journal_voucher'",(int(entry_id),)).fetchone()
                if not existing: raise KeyError(entry_id)
                self._assert_period_open(existing["entry_date"]); voucher_number=str(item.get("entry_number") or existing["entry_number"]).strip()
                duplicate=db.execute("SELECT 1 FROM journal_entries WHERE entry_number=? AND id<>?",(voucher_number,int(entry_id))).fetchone()
                if duplicate: raise ValueError("Voucher number already exists")
                db.execute("UPDATE journal_entries SET entry_number=?,entry_date=?,description=?,currency=?,branch_id=?,voucher_type=? WHERE id=?",(voucher_number,date,description,currency,branch_id,voucher_type,int(entry_id)))
                db.execute("DELETE FROM journal_lines WHERE entry_id=?",(int(entry_id),)); saved_id=int(entry_id); action="update"
            else:
                voucher_number=str(item.get("entry_number") or "").strip()
                if not voucher_number:
                    year=self._date_year(date); prefix=f"JV-{year}-"; row=db.execute("SELECT entry_number FROM journal_entries WHERE entry_number LIKE ? ORDER BY entry_number DESC LIMIT 1",(prefix+"%",)).fetchone()
                    sequence=int(row["entry_number"].rsplit("-",1)[-1])+1 if row else 1; voucher_number=f"{prefix}{sequence:06d}"
                if db.execute("SELECT 1 FROM journal_entries WHERE entry_number=?",(voucher_number,)).fetchone(): raise ValueError("Voucher number already exists")
                saved_id=db.execute("INSERT INTO journal_entries(entry_number,entry_date,description,source_type,currency,branch_id,created_by,created_at,voucher_type) VALUES(?,?,?,?,?,?,?,?,?)",
                    (voucher_number,date,description,"journal_voucher",currency,branch_id,user_id,utcnow(),voucher_type)).lastrowid; action="create"
            for code,line_description,debit,credit,extra,raw_line in normalized:
                department_id,project_id=self._dimension_ids(db,{"department":raw_line.get("department") or item.get("department"),"project":raw_line.get("project") or item.get("project"),
                    "department_id":raw_line.get("department_id") or item.get("department_id"),"project_id":raw_line.get("project_id") or item.get("project_id")})
                account=db.execute("SELECT id FROM accounts WHERE code=?",(code,)).fetchone()
                if not account: raise ValueError(f"Account {code} was not found")
                party=db.execute("SELECT id FROM parties WHERE account_number=?",(code,)).fetchone()
                db.execute("""INSERT INTO journal_lines(entry_id,account_id,party_id,description,debit,credit,line_currency,amount,amount_lbp,amount_usd,rate_lbp,rate_usd,due_date,reference,department_id,project_id)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(saved_id,account["id"],party["id"] if party else None,line_description,str(debit),str(credit),
                    *( (extra["line_currency"],str(extra["amount"]),str(extra["amount_lbp"]),str(extra["amount_usd"]),str(extra["rate_lbp"]),str(extra["rate_usd"]),extra["due_date"],extra["reference"],department_id,project_id) if extra else (None,None,None,None,None,None,None,None,department_id,project_id) )))
                if department_id or project_id:
                    db.execute("UPDATE journal_lines SET department_id=?,project_id=? WHERE id=last_insert_rowid()",(department_id,project_id))
            db.execute("INSERT INTO audit_log(user_id,action,entity,entity_id,details,created_at) VALUES(?,?,?,?,?,?)",(user_id,action,"journal_voucher",saved_id,json.dumps({"entry_number":voucher_number,"description":description}),utcnow()))
        return self.journal_voucher_detail(saved_id)
