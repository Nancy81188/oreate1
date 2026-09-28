# Saber Accounting MVP

## Version 2.9.7 (Independent Department and Project controls)

- Departments and Projects now each have their own visibility checkbox in their respective Security data sheets. Either field can be hidden independently in entry forms, report filters, and Journal Voucher without deleting saved values. The application title matches the installer version.

## Version 2.9.6 (Department and Project visibility)

- The Departments and Projects data sheets under Security each have a Show Department / Project checkbox for entry forms, budget and report filters, and the Journal Voucher sheet.
- Hiding fields only changes the display; saved department and project data remains intact. Report filters return to All when hidden so an unseen filter cannot narrow the report.

## Version 2.9.5 (Journal entry and shared-server login protection)

- In Journal Voucher, the first letter selects a currency in the voucher header and the line currency cell. The line detail copies into the next line; editing the next line leaves the first unchanged.
- New Account in Journal Voucher creates an account immediately and places it on an available line without saving the voucher. Accounts created on the Accounts page are immediately recognized by an already-open Journal Voucher.
- Failed logins are audited without passwords or tokens. Five failures per username or 30 per client IP within 15 minutes trigger a 15-minute lockout; the server returns HTTP 429 while blocked.
- The shared server accepts a trusted TLS certificate and key. Plaintext is limited to localhost unless `--allow-insecure-lan` is deliberately specified for a trusted VPN/LAN.

## Version 2.9.4 (Equal height navigation rows)

- Navigation tabs in every row share the same height, including rows with labels that wrap onto two lines.

## Version 2.9.3 (Navigation and invoice controls alignment)

- The navigation tabs have visible spacing, stretch across the application window and automatically wrap into more rows as the window gets narrower; horizontal scrolling remains available on exceptionally narrow windows.
- On Uploaded Data, the Branch selector and both rows of invoice action buttons begin at the left edge below the table.

## Version 2.9.2 (Payroll registration worksheet)

- Employee files now retain nationality, parents' names, date of birth and place of birth. Existing company files add these empty fields automatically without changing saved payroll.
- Employees > R3 Registration Worksheet can preview, export PDF or export Excel with the saved employee details and highlights missing information. This worksheet helps prepare the Ministry of Finance's R3 new-employee registration; it is not the official form or an electronic submission. Complete the official form and its supporting documents separately.
- Employees has download buttons for the original Ministry of Finance R3 and R3-1 PDF forms. The original blank forms are downloaded from the Ministry website when requested.
- NSSF contributions report lists the employees in the selected period, counts both registered employees and employees with payroll, and shows missing NSSF numbers. The report's Employee List / Edit button opens the editable employee list.
- Payroll > Official Reports > SETTLEMENT builds an annual NSSF reconciliation from posted payroll. Use Filed NSSF Wages to enter the wages already declared for each month and actual payments; unknown values stay blank and the settlement remains incomplete. The difference uses the effective rates saved for each month. The entries have an audit log and do not post a journal voucher automatically.
- The original blank CNSS contributions, annual settlement and annual employee declaration PDFs can be downloaded from the CNSS links. Those public templates show a preprinted 9% sickness rate; compare the template with the period's saved rates before submission. The application's reconciliation is a review worksheet, not an official CNSS filing.
- The Employee File dialog scrolls on smaller screens, with Save always visible.
- Main navigation grows to fit both rows of tabs; outer page scrollbars appear only when the content exceeds the available space.

## Version 2.9.1

- Main window opens within the available screen dimensions and its minimum size respects smaller displays.
- Every main page now has vertical and horizontal scrollbars so forms, tables, and action buttons remain reachable on smaller screens or with larger Windows display scaling. The two-row navigation can scroll horizontally as well.
- General Journal action buttons and totals now appear above the table, so they are immediately visible instead of being squeezed against the bottom of the window.

## Version 2.9.0

- **Bank Reconciliation** (Payment & Receipt > Bank Reconciliation): import the bank statement (Excel or CSV: Date, Description, Reference, Debit / Credit or Amount) for a bank account (511 / 512 / 519 / 53), Auto Match (same amount, dates within 5 days), Match / Unmatch by hand, post statement-only items (bank charges 6739, interest...) as a voucher that is matched at once, and the reconciliation: book balance, deposits not yet at the bank, payments not yet cleared, statement items not booked, expected bank balance and the difference with the statement balance. Report in PDF / Excel / print.
- **Dashboard charts** for the fiscal year (USD or LBP): sales vs purchases and expenses by month, receivables by age, top 5 clients, cash and bank balances.
- **AI_RULES.md**: the rules for anyone (people, ChatGPT, Claude) who changes the program - start from the latest version, never remove features or tests, run the tests, deliver the whole project, accounting rules.
- VAT declaration box numbers: kept as the section layout (A / B / C / E / F) until the official Ministry of Finance form is provided.

## Version 2.8.3 (review)

- New currencies (for example SAR) now work everywhere: payroll converts LBP -> USD -> the new currency when there is no direct rate, and VAT adjustments accept any currency set up under Exchange Rates.
- Layout at 1366 x 768: "Due days from invoice" moved so its box is visible on Customers / Suppliers; Sales Invoice "Amount Paid", "Branch" and "VAT Treatment" moved to their own row so nothing is cut off.

## Version 2.8.2

- Purchase Invoice actions sit beside the shorter entry form; the item table has more height and a wider description column.
- In Inventory Reports, Stock Card has Item From / Item To selectors and the existing date From / To fields. The Ageing buckets entry box is removed; Stock Ageing uses its standard ageing buckets.
- The main navigation takes less space above the working area.
- Customer / Supplier Ageing lists invoice due dates and overdue days. Business Reports has Today and +30 days shortcuts and an expected collection/payment summary due by the chosen as-of date.
- Inventory Analysis (3D) compares item/category/supplier by warehouse or month, using quantity or cost value. Inventory Health lists stock issues needing review, including reorder levels, missing supplier or unit cost, and no recent issue.
- The Customers / Suppliers page links directly to Customer / Supplier Ageing and Client Items: Qty & Value; the latter lists each client's purchased items, quantity, sales before VAT, VAT, and TTC.

## Version 2.8.1

- Customer and supplier files include **Due days from invoice**. New invoices automatically use invoice date plus the saved term when Due Date is blank; an explicit Due Date takes precedence. Existing invoices keep their saved due dates.
- Purchase Invoice header is shorter so more item rows fit. Cost on Purchase uses predefined expense accounts, with an Edit Cost Accounts dialog for a particular posting.
- Inventory Reports adds Stock Turnover, Stock by Supplier, and Physical Count Variances. Stock Ageing can filter by item; Stock Card continues to use the selected item and From/To dates. Physical Inventory can add an item to its count sheet.
- Each manually entered exchange rate is saved separately. The daily rate used in reports is the arithmetic mean of entered rates for that date and currency pair. Automatic reference rates no longer overwrite a manual daily average.

Saber Accounting is a Windows desktop accounting application with a central shared database for three users. This first version includes:

- English, Arabic, and French interface
- Automatic USD, EUR, LBP, and AED detection from currency and amount cells
- Missing currency defaults to USD; conflicting or unsupported currencies are flagged for review
- Currency filter for the dashboard, invoices, trial balance, and exported reports
- Lebanese VAT at 11%
- Purchase and sales invoice import from Excel
- Manual purchase and sales invoice entry with multiple items
- Invoice deletion retains the invoice number and marks it DELETED; it removes the journal and stock effect. Linked allocations and active dependent invoices must be resolved first.
- Purchases and sales show gross total, discount, total after discount before VAT, VAT, and final total. Purchase discounts reduce the posted invoice amount and stock line costs.
- Journal Voucher Find searches each line's detail; each line detail can be edited in its own table column.
- Bank commissions on receipts and payments post to the nine-digit account 673900000.
- Stock Card accepts an item and From Date / To Date and includes the range in the report heading.
- Stock Ageing groups the on-hand value by receipt date in configurable ageing buckets, as of the selected To Date.
- Trial Balance can show EUR and AED equivalents as either reporting column. Add a three-letter currency under Security / Backup / Rates → Exchange Rates, then enter its exchange rate before cross-currency reporting.
- The dashboard uses compact currency summaries; purchase invoice entry keeps the items and totals on one page, while landed costs have a separate tab.
- Optional AI buttons suggest expense accounts and preview page 1 of a PDF invoice. The existing local account suggestion and PDF reader work without AI. For online assistance enter an OpenAI API key when prompted (kept in memory for that session), or set `SABER_AI_API_KEY` before starting the app. Each request needs confirmation, sends the description or first PDF page to OpenAI, may incur API charges, and never saves an invoice automatically. Review all amounts and the account before Save.
- Automatic 11% VAT per item, with editable VAT rate and VAT amount
- Editable total before VAT per item with automatic invoice totals
- Original invoice number when supplied; otherwise original Excel row number
- Completely empty rows skipped; duplicate invoices retained
- Automatic double-entry journal posting
- Invoice register, dashboard, and trial balance
- User authentication, roles, audit log, customer/supplier, inventory, and stock database foundations

## Important status

This is an MVP for controlled testing. TLS is available for shared access but requires a trusted certificate and secure server configuration. Fiscal-year closing blocks later edits, while finer monthly period locks remain to be added. Before production use, complete encrypted backup and restore, exchange-rate revaluation, and independent validation of Lebanese tax/NSSF reporting by the firm's accountant.

## Quick start on one computer

Install Python 3.11 or newer. Open Command Prompt in this folder and run:

```bat
python -m pip install -r requirements.txt
python run_server.py --admin-password YourStrongPassword
```

Open a second Command Prompt in the same folder:

```bat
python run_desktop.py
```

Sign in with username `admin`, your chosen server password, and server address `http://127.0.0.1:8765`.

## Three synchronized computers

1. Choose one always-on office computer or Windows server to host the shared database.
2. Give that computer a fixed local IP address.
3. Allow TCP port `8765` only on the trusted office network. Provision a certificate whose name matches the host name used by clients and whose CA is trusted on their computers.
4. Run `python run_server.py --host SERVER-IP --tls-cert server-cert.pem --tls-key server-key.pem` only on the server computer. Keep the private key restricted to the server account.
5. Run the desktop client on each of the three computers.
6. Enter `https://SERVER-NAME:8765` on the sign-in screen, using the name on the certificate.

For access outside the office, do not expose port 8765 directly to the internet. Use a professionally configured HTTPS reverse proxy or VPN. When TLS terminates at a reverse proxy, bind the Python server to `127.0.0.1` and proxy only to that loopback address. Existing trusted VPN/LAN installations that intentionally need plaintext must pass `--allow-insecure-lan`; HTTP traffic on such networks exposes passwords and tokens to anyone able to observe it.

## Excel import rules

The first worksheet is imported. Recognized English, Arabic, and French headings include Invoice Number, Date, Supplier/Customer Name, Total Before VAT, VAT, Total After VAT, Currency, and Type.

- If an invoice-number column contains a value, that value is used.
- Otherwise the original Excel row number is used. Excel row 24 becomes invoice 24.
- Completely empty rows are ignored.
- Duplicate invoices are deliberately retained.
- The original filename and Excel row number are stored for audit tracking.
- Missing VAT is calculated at 11% when the subtotal exists.
- Existing VAT values are preserved, even when they differ from 11%.
- Source totals that do not equal subtotal plus VAT are preserved, marked `review`, and posted against Import Variance so the ledger remains balanced.

## Build the Windows executable

On Windows, after installing the requirements:

```bat
pyinstaller --noconfirm --onefile --windowed --name SaberAccounting run_desktop.py
pyinstaller --noconfirm --onefile --name SaberAccountingServer run_server.py
```

The executables will be created in the `dist` folder. No GitHub account is required.

## Build a one-click installer online

Upload this project to a private GitHub repository. The included workflow runs the tests, creates the standalone client and server, and packages them as `SaberAccountingSetup.exe`. Open the repository's Actions tab, select **Build Saber Accounting Installer**, run the workflow, and download the **SaberAccountingSetup** artifact. End users do not need Python or GitHub.

## Version 0.7.1 fresh start

The default server database is `SaberAccounting/saber_accounting_v0_7.db`. This gives the upgraded application a completely fresh company file with only the default admin account. The previous `saber_accounting.db` is not loaded and remains available as a safety archive. New entries in v0.7.1 persist normally after the application is closed and reopened.

## Version 0.7.2 Excel currency formats

Excel imports detect USD, EUR, LBP, and AED from both cell contents and Excel Accounting/Custom number formats. This supports sheets where currency symbols are displayed beside numeric values without a separate Currency column. Imported dashboards, invoice lists, trial balances, and exports remain separated by currency.

## Version 0.7.3 currency page filter

The Import Excel preview includes an All/USD/EUR/LBP/AED selector and Apply button. Only rows assigned to the selected currency are displayed. Blank cells with leftover number formatting are ignored during detection; genuinely mixed rows are assigned using Total, Before VAT, and VAT evidence and remain flagged for review.

## Version 1.12.0 final release

### Payroll official reports (Payroll > Official Reports)
- **R10** quarterly salary tax withholding, **R5** annual employer declaration, **R6** individual annual statement.
- Any **month, quarter or year**; employees and managers in **separate sections**, plus a grand total.
- NSSF **employee 3%** and employer medical, family and end-of-service contributions.
- Rates and ceilings are **effective-dated (Date From to Date To)**: each month uses the rules in force on its own date. Saving a new Date From automatically ends the previous period the day before; overlapping periods are rejected.
- Separate columns for **retro salary (with its own retro tax)**, transport, schooling, bonus and 13th salary. R6 shows each retro period.
- Official amounts in LBP (other currencies converted at the payroll month's rate). Posted payroll only, with an optional draft preview.
- **Excel and PDF** export.

### Quarterly VAT (Quarterly VAT tab)
- **Q1-Q4** dates set automatically.
- Sales (output) VAT; deductible VAT on purchases, fixed assets, expenses and customs/imports; **non-deductible VAT** shown separately.
- VAT **payable or credit** carried forward to the next quarter (including into Q1 from the previous fiscal-year file).
- Totals **by currency with LBP equivalents**.
- **Manual adjustments** with a mandatory reason. Saving a return locks the quarter; only an administrator can reopen it.
- Marking VAT non-deductible (Uploaded Data > "VAT Deductible / Non-Deductible", or the expense checkbox) moves that VAT into cost, so the ledger always equals the return.
- **Excel and PDF** export.

### Security and polish
- New non-admin users are valid for **1 year** ("Renew 1 Year" in Security > Users). Expired users cannot sign in. Sessions end after 24 hours.
- Per-user **Payroll** and **VAT** access. At least one active administrator is always kept.
- **Legal document alerts** at sign-in and from the header button, for expired documents and documents expiring within 30 days.
- Backups use SQLite's online backup (safe while others work). Restore validates the file and creates a safety backup first.
- Clearer error messages. A page that fails to load no longer stops the others.

### Fixes
- Payroll saved from the desktop app now stores the period correctly (this previously affected payroll numbering and rate lookups).
- Exchange-rate lookups now pick the latest rate on or before the date, chronologically.
- Users created in Settings are saved to the sign-in database.

### To confirm with your accountant
The salary tax method is unchanged: transport and schooling are included in taxable salary, and one-off bonus / 13th salary are annualized ×12 in the month paid. Adjust in Tax & NSSF Settings or ask for a rule change if your practice differs.

### Build the installer (final workflow)
1. Upload this project to the GitHub repository (replace the old files).
2. Open **Actions**, select **Build Saber Accounting Installer**, click **Run workflow**. It also runs automatically on every push to `main`.
3. When it finishes, download the **SaberAccountingSetup** artifact and run `SaberAccountingSetup.exe`.

One installer only: no Python, no manual server. The data service starts automatically inside the app, and company data stays in the user's `SaberAccounting` folder across upgrades. First sign-in on a new computer: `admin` / `admin` (change it in Security > Users).


---

# Version 2.0.0 - complete release

## Modules
| Tab | What it does |
|---|---|
| Sales Invoice | Automatic number, editable lines (Item, description, qty, price, VAT), VAT treatment (taxable / zero-rated / exempt / out of scope), New / Save / Save & Post, reopen and edit |
| Journal Voucher | BRAINS-style voucher: multi-currency lines with LBP and USD amounts and rates, due date, reference, department, project, navigation |
| Import | Excel or PDF invoices as Purchases, Sales, Expenses or Assets. PDFs are read automatically and attached. Adds to existing data (replace is optional) |
| Customers / Suppliers | Account number first; type 4 digits and the full number fills in |
| Payment & Receipt | Customer receipts (RV-) and supplier payments (PV-) on the page, with balance, edit and delete |
| Purchases & Expenses | Purchases with PDF, cost on purchase (customs, freight, insurance, import VAT - manual, Excel or PDF), VAT use; expenses with PDF, Excel import, New / Edit / Delete / Search |
| Inventory | Items, warehouses, stock documents (opening, receipt, issue, adjustments, transfer), weighted average or FIFO, reports, stock variation |
| Payroll | Lebanese rules 2024-2026, R5 / R6 / R10 reports |
| Quarterly VAT | Lebanese periodic declaration with the partial deduction right |
| Trial Balance / Statement | Balance des Comptes options (BRAINS) |
| Profit & Loss | Fiscal-year dates, closing 6 & 7 as a Journal Voucher, automatic opening of the next year |
| Financial Reports | Ledger, balance sheet, cash flow, aging, comparative P&L, budget |
| Security / Backup / Rates | Users with 1-year validity and permissions, departments, projects, backups, exchange rates |

## Inventory (Lebanese periodic method)
- Purchases stay in 601. Stock quantities and costs come from the stock documents.
- Costing: weighted average (default) or FIFO. Stock can never go negative in a warehouse.
- A Sales Invoice line with an Item code issues the stock automatically (Stock Issue linked to the invoice; deleting or cancelling the invoice removes it).
- Reports: Stock Valuation (at any date, by warehouse, at cost and at sales price), Stock Card, Stock Movements, Sales Margin (COGS), Reorder, Slow-moving stock. Excel, PDF and print.
- Year end: the Stock Variation voucher (type 06) cancels account 37 against 6051 and books the closing stock (Dr 37 / Cr 6052). It is posted automatically when the year is closed, and the closing stock becomes the Opening Stock of the next year.

## Year-end order
1. Enter the last documents of the year and check the stock (Inventory > Reports > Stock Valuation at 31-12).
2. Profit & Loss > Preview Closing 6&7.
3. Close the year: stock variation, closing 6 & 7 (result to 121 / 125), and the opening of the next year (balances and stock) are made automatically.
4. "Delete Closing & Reopen Year" undoes everything if a correction is needed.

## Points to confirm with the accountant
- Employer NSSF sickness & maternity rate (8% per PwC; one source says 11%).
- Exact start dates of Jan-Feb 2024 ceilings and the 28M minimum wage.
- VAT declaration box numbers against the official MoF form; rounding of the deduction ratio.

# Version 2.1.0

## Arabic in PDF
Every PDF (reports, statements, invoices, VAT declaration, R5 / R6 / R10, NSSF statement) prints Arabic text correctly - joined letters, right-to-left - using the Amiri font (SIL Open Font License, `assets/fonts/Amiri-OFL.txt`). Official reports carry Arabic labels next to the English.

## NSSF ceilings - automatic and monthly
- A new or never-configured company loads the Lebanese periods 2024-2026 automatically (ceilings, rates, family allowances, tax rounding). Settings you changed yourself are never overwritten; "Load Lebanese Law 2024-2026" reloads them on request.
- Payroll is monthly: each payroll uses the rules in force on the **last day of its month** (for example the 90M -> 120M ceiling change of August 2025, or the LBP 10,000 rounding from 25-11-2024 for November). Retroactive pay uses the ceilings of each of its own months.
- Payroll > Official Reports > "CEILINGS - NSSF ceilings by month" shows the ceilings and rates of every month of a year.

## NSSF payment format
Payroll > Official Reports > "NSSF - Contributions statement (payment)", monthly or quarterly, Arabic / English:
- per employee and month: NSSF number, salary subject, capped bases and contributions for sickness & maternity (employee 3% + employer), family allowances (6%) and end of service (8.5%), family allowances already paid, net due;
- payment summary by branch and the net amount payable to the NSSF (LBP);
- the monthly ceilings and rates applied; employer NSSF number from General Settings.
"Record NSSF Payment" books the payment voucher (Dr NSSF payable / Cr cash or bank).

## Fix
Company files created by older versions are brought up to date automatically when they are opened.

# Version 2.2.0

## Sales Invoice, Debit Note, Credit Note
- Document type: Invoice (SAL-), Debit Note (DN-), Credit Note (CN-, reverses the sale and reduces the VAT of the period).
- Lines: Item, Description, Qty, Unit, Unit Price, Total Amount, Discount %, VAT %, Net.
- Totals: Total, Discount (% or amount), **Total HT**, VAT 11% (struck through for zero-rated / exempt), TOTAL, and the **amount in words** in English and Arabic (tafqeet).
- Find by number only (type 12 for SAL-2026-000012), Duplicate, Print Preview, PDF, Print, Import Excel (template provided), Import PDF, Excel Template.

## General Journal
Find by voucher number and by details; Print Preview, PDF and Print.

## Payment & Receipt
Cash / bank accounts from 511, 512, 519 and 53 only; customers and suppliers in both tabs; **allocation** of each receipt / payment to open invoices (auto: oldest first), open balance per document.

## Purchases & Expenses
- Find instead of the lists. Purchases: items received into stock with warehouse (F2 item search; an item that does not exist is created automatically), Excel import with template, PDF.
- Cost on purchase: each cost to its own 9-digit 6018 account (601800001 freight, 601800002 insurance, 601800003 customs duties, 601800004 broker, 601800005 other); import VAT to 44210.
- Expense account chosen from accounts 626 to 69.

## Accounts
VAT: 44210 purchases, 44211 export-related purchases, 44216 expenses, 4427 sales. Payroll: 6311 salaries, 6312 bonus / 13th, 6313 commission, 6315 schooling, 6316 managers' salaries, 6319 transport, 4411 salary tax, 4431 NSSF.
Year-end result to **138** (profit) / **139** (loss); the closing voucher is "CLOSING 6&7" in the General Journal.

## Inventory
Items with cost price (average of purchases), supplier, category / subcategory, unit and location. New tabs: Categories & Units, Stock In / Stock Out (at average cost), Physical Inventory (stock on hand, count, difference, save, print, Excel sheet, upload, post the differences). Reports filter by category, subcategory, unit, supplier and warehouse together.

## F2
F2 opens the list that fits the field: items in item fields, customers / suppliers in party fields, accounts elsewhere.

# Version 2.3.0 - Statement of Account / Trial Balance
- Account From / To: search by number or name among all accounts (parents too); the account name shows beside each box (like BRAINS). "Same as From" copies the account.
- The options are in their own "Options" tab; every Show opens its own full-page tab with Print Preview, Print, Excel, PDF and Close Tab. Several statements can stay open side by side.
- Double-click a statement line to see the transaction (all its lines) and "Open in its screen" (journal voucher, sales invoice, purchase, receipt / payment, expense). In the Trial Balance, double-click an account to open its statement in a new tab.

# Version 2.4.0
- Profit & Loss > "Delete Year" (administrators): deletes the last fiscal year of a company (for example 2025, to redo the opening). A backup copy of the file is kept in `companies/<company>/deleted_years`, and the previous year is reopened with its closing removed. Type "DELETE <year>" to confirm. Then close the previous year again to make a new opening.
- NSSF statement: sickness & maternity shown as employee 3% + employer 8% = total 11% (as in the NSSF declaration).

# Version 2.5.0 - Backups per company and per year
- Backups are made automatically each day while signed in to Windows. You can also press "Create Backup Now"; safety backups are made before restore and replacement imports.
- Each company and each fiscal year has its own folder and file name: `SaberAccounting\backups\<Company>\<Year>\<Company>_<Year>_<date>_<time>.db`.
- Security / Backup / Rates > Backup & Restore shows the backups of the company and year you are in, with "Save Backup As..." (copy to a USB key or a drive folder) and "Open Backup Folder". Backups made by older versions still appear and can be restored.

# Data safety and automatic backups update

- The first standalone launch asks you to set an admin password. Existing installations keep their current password.
- Any signed-in user can create, view, and save a backup of the selected company/year from **My Backups**. Only administrators can restore a backup.
- The Windows installer installs a background backup process in the shared Startup folder. It runs after Windows sign-in, checks once per hour, and creates one backup per company/year when 24 hours have passed. The desktop window does not need to be open. The computer must be on and a Windows user must be signed in. On the first new-company launch, a backup is made immediately. Backup files live in `SaberAccounting/backups/<Company>/<Year>` under that Windows user's profile; copy this folder to another drive if you need protection from drive failure.
- Replacing imported invoices now validates the complete batch before changing the live file and keeps manual journal vouchers. If any row fails, the replacement is cancelled. A safety backup is made before a successful replacement.
- Replacement is refused when payments, stock documents, or a saved VAT return are linked to existing invoices, when a fiscal year is closed, or when existing invoices record amounts paid. Review those records first.
- Invalid company/year selections return an error. Payment and expense edits are prepared on a database snapshot before replacing the live file. Stock checks no longer temporarily remove saved movements.
- The PDF import preview scans every page and creates separate preview rows when invoice numbers change. Repeated invoice numbers on following pages are grouped. Scanned pages stay visible for manual entry. Invoices sharing one page still require manual separation and review.

# Version 2.6.0 - review of the ChatGPT changes + inventory reports
Kept from the ChatGPT changes (all tests pass): initial admin password (10+ characters) instead of admin/admin, safer invoice / payment edits (nothing lost if a save fails), year closing with automatic rollback, stricter company / year checks, local expense-account suggestions (ai_mapper) and optional OpenAI assistance (ai_service - needs an API key; it sends page 1 of the chosen invoice PDF to OpenAI).
Adjusted: the background daily backup is now an OPTIONAL installer task, unchecked by default (backups are made on request from Backup & Restore); leftover files removed (temp.txt, shortcut).

## Inventory reports
- **Inventory Summary**: key figures (items, value at cost and at sales price, potential margin, items to reorder, slow-moving and old-stock value), value by category and by warehouse, top 10 items, ageing, items to reorder.
- **Stock Ageing**: stock on hand by age of receipt (first in - first out): 0-30, 31-60, 61-90, 91-180, 181-365, over 365 days (buckets can be changed), value per bucket, average age, oldest receipt, last issue, % of old stock, category subtotals, ageing summary, and the list of stock older than 180 days to review.
- **Stock Valuation**: grouped by category with subtotals.
All with the filters (warehouse, category, subcategory, unit, supplier, costing method) and Excel / PDF / Print.

# Version 2.7.0
- Merged: the latest ChatGPT changes + version 2.6.0 (stock ageing, inventory summary, valuation by category, optional automatic backup were missing from the upload and are back).
- **Financial Reports > Business Reports** (Excel, PDF, print, preview):
  - Receivables Ageing (customers) and Payables Ageing (suppliers): open documents by days after the due date (not due, 1-30, 31-60, 61-90, 91-180, over 180 - buckets can be changed), receipts / payments not allocated, net due, % overdue, detail of open documents.
  - Item Sales by Client, and Client Quantities by Item: quantity, average price, HT, VAT, TTC.
  - Sales Analysis (3D pivot): rows (client / item / category) x columns (month / quarter / client / item / category) x measure (quantity / HT / VAT / TTC).
  - Top Clients and Top Suppliers (purchases and expenses): HT + VAT = TTC, share, cumulative share, number of documents.
  - Amounts in USD or LBP (converted at each document date) or one currency only; credit notes deducted.
- **Payroll > Tax & NSSF Settings**: the NSSF ceilings and rates by period (Date From - Date To) are edited directly in the table (double-click), with Add / Delete / Save Periods; a new Date From closes the previous period automatically.
- Lighter, calmer layout: shorter table rows (more lines on screen), soft headings, clean input borders, buttons that light up under the mouse.
