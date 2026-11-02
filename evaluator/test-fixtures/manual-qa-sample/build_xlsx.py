#!/usr/bin/env python3
"""Generates the sample .xlsx files (templates and the trainee's outputs) with the
standard library only. Re-run to regenerate:  python build_xlsx.py
Row 1 is the title, row 3 the header, data from row 4. The Bug List keeps a Severity and
a Priority dropdown, like the course template."""
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
SUB = HERE / "submission"


def col(i):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]


def write_xlsx(path, sheet, title, headers, rows, dropdowns=None):
    def cell(r, c, v):
        return f'<c r="{col(c)}{r}" t="inlineStr"><is><t>{escape(str(v))}</t></is></c>'
    xml_rows = [f'<row r="1">{cell(1, 0, title)}</row>',
                f'<row r="3">{"".join(cell(3, i, h) for i, h in enumerate(headers))}</row>']
    for n, row in enumerate(rows, start=4):
        xml_rows.append(f'<row r="{n}">{"".join(cell(n, i, v) for i, v in enumerate(row))}</row>')
    dv = ""
    if dropdowns:
        items = "".join(
            f'<dataValidation type="list" allowBlank="1" sqref="{col(headers.index(h))}4:{col(headers.index(h))}200">'
            f'<formula1>"{",".join(opts)}"</formula1></dataValidation>' for h, opts in dropdowns.items())
        dv = f'<dataValidations count="{len(dropdowns)}">{items}</dataValidations>'
    widths = "<cols>" + "".join(f'<col min="{i+1}" max="{i+1}" width="24" customWidth="1"/>' for i in range(len(headers))) + "</cols>"
    sheet_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                 f'{widths}<sheetData>{"".join(xml_rows)}</sheetData>{dv}</worksheet>')
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   f'<sheets><sheet name="{escape(sheet)}" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)


TR_H = ["AC ID", "Acceptance Criteria", "TR ID", "Test Requirements", "Notes"]
TC_H = ["TR ID", "TC ID", "TC Summary", "Pre-Condition", "Steps", "Expected Result", "Notes"]
BUG_H = ["ID", "Summary", "Description", "Pre-Condition", "Steps to Reproduce", "Screenshot", "Build found",
         "Reproducibility", "Severity", "Frequency", "Priority", "Keyword", "Status", "Note"]
DD = {"Severity": ["Critical", "Major", "Minor", "Trivial"], "Priority": ["High", "Medium", "Low"]}

TR_TITLE, TC_TITLE, BUG_TITLE = "Requirements Traceability Matrix", "Test Case List", "Bug List"

# templates inside the skills (the Test-Case-Generation one is deliberately under references/)
write_xlsx(SUB / "skills/test-requirements-analysis/assets/tr-template.xlsx", "Test Requirement", TR_TITLE, TR_H, [])
write_xlsx(SUB / "skills/Test-Case-Generation/references/tc-template.xlsx", "TC List", TC_TITLE, TC_H, [])
write_xlsx(SUB / "skills/defect-analysis-reporting/assets/bug-template.xlsx", "Bug List", BUG_TITLE, BUG_H, [], DD)

AC2 = "Invalid credentials show an error and stay on the login page"
TR_ROWS = [
    ["AC1", "Valid credentials redirect to /notes", "TR-01", "A user with valid credentials is redirected to /notes", ""],
    ["AC2", AC2, "TR-02", "A wrong password shows an error and stays on the login page", ""],
    ["AC2", AC2, "TR-03", "An unknown email shows an error and stays on the login page", ""],
    ["AC3", "Empty email shows 'Email is required'", "TR-04", "An empty email shows 'Email is required' under the field", ""],
    ["N/A", "", "TR-05", "An email made only of spaces is rejected", "Edge case"],
    ["N/A", "", "TR-06", "The 5th consecutive failed attempt locks the account", "Edge case"],
    ["N/A", "", "TR-07", "A correct password entered during the lock is rejected", "Edge case"],
    ["N/A", "", "TR-08", "Password length and complexity rules are validated", "Missing info"],
    ["N/A", "", "TR-09", "The error message must not reveal whether an email is registered", "Risk"],
]
TC_ROWS = [
    ["TR-01", "TC-01", "Login with valid credentials", "User user1@example.com / Passw0rd! exists",
     "1. Open the login page\n2. Enter user1@example.com\n3. Enter Passw0rd!\n4. Click Login",
     "The browser navigates to /notes and the notes list is displayed", ""],
    ["TR-02", "TC-02", "Login with a wrong password", "User user1@example.com exists",
     "1. Open the login page\n2. Enter user1@example.com\n3. Enter Wrong#123\n4. Click Login",
     "The message 'Invalid email or password' is shown above the form and the URL stays /login", ""],
    ["TR-03", "TC-03", "Login with an unknown email", "No user nobody@example.com",
     "1. Open the login page\n2. Enter nobody@example.com\n3. Enter Passw0rd!\n4. Click Login",
     "The message 'Invalid email or password' is shown and the URL stays /login", ""],
    ["TR-04", "TC-04", "Login with an empty email", "Login page is open",
     "1. Leave the email empty\n2. Enter Passw0rd!\n3. Click Login",
     "Error is displayed correctly", ""],
    ["TR-05", "TC-05", "Login with a spaces-only email", "Login page is open",
     "1. Enter three spaces in the email field\n2. Enter Passw0rd!\n3. Click Login",
     "The field shows 'Email is required' and the form is not submitted", ""],
    ["TR-06", "TC-06", "The 5th failed attempt locks the account", "User user2@example.com exists and is not locked",
     "1. Enter user2@example.com with Wrong#123 and click Login, five times in a row",
     "After the 5th attempt the message 'Account locked for 15 minutes' is shown and the Login button is disabled", ""],
    ["TR-08", "TC-07", "Password length validation", "Login page is open",
     "1. Enter user1@example.com\n2. Enter abc\n3. Click Login",
     "Shows the error 'Password must be 8-20 characters'", ""],
    ["TR-09", "TC-08", "Error message does not reveal registered emails", "User user1@example.com exists",
     "1. Log in with user1@example.com and Wrong#123 and note the message\n2. Log in with nobody@example.com and Passw0rd! and note the message",
     "Both attempts show the identical message 'Invalid email or password'", ""],
    ["TR-11", "TC-09", "Login after the lock expires", "Account user2@example.com was locked 16 minutes ago",
     "1. Enter user2@example.com\n2. Enter Passw0rd!\n3. Click Login",
     "Success", ""],
]
BUG_ROWS = [
    ["BUG-001", "Account locked after 4 failed attempts",
     "Expected: the account locks after the 5th failed attempt (AC4). Observed: it locks after the 4th.",
     "User user2@example.com exists", "1. Open /login\n2. Enter user2@example.com with Wrong#123 and click Login, four times",
     "lock-4th.png", "v1.4.2", "Always", "Major", "Every account", "High", "lock", "New",
     "Severity Major: users are locked out earlier than specified. Priority High: affects every user. Browser: Chrome 126. OS: not provided."],
    ["BUG-002", "Error message reveals that an email is not registered",
     "Expected: a generic message for any failed login. Observed: 'Email not registered' is shown for an unknown email.",
     "No user nobody@example.com", "1. Open /login\n2. Enter nobody@example.com and Passw0rd!\n3. Click Login",
     "unknown-email.png", "v1.4.2", "Always", "Trivial", "Every unknown email", "Low", "error message", "New",
     "Severity Trivial: it is only wording. Priority Low: cosmetic. Browser: Chrome 126. OS: Windows 11."],
    ["BUG-003", "Empty email gives no validation message",
     "Expected: 'Email is required' under the field (AC3).",
     "Login page is open", "1. Leave the email empty\n2. Enter Passw0rd!\n3. Click Login",
     "empty-email.png", "v1.4.2", "Always", "Minor", "Every empty submit", "Medium", "validation", "New",
     "Severity Minor: the user is not told why nothing happens. Priority Medium: easy to hit. Browser: Chrome 126. OS: not provided."],
]
write_xlsx(SUB / "outputs/tr-list.xlsx", "Test Requirement", TR_TITLE, TR_H, TR_ROWS)
write_xlsx(SUB / "outputs/tc-list.xlsx", "TC List", TC_TITLE, TC_H, TC_ROWS)
write_xlsx(SUB / "outputs/bug-list.xlsx", "Bug List", BUG_TITLE, BUG_H, BUG_ROWS, DD)
print("wrote 6 xlsx files")
