# Chat transcript (sample trainee, built from the trainer's baseline)

> Two skills are installed: `test-requirements-analysis` and `test-case-generation`.

---

## Turn 1: requirements analysis

**User:** I attached `User Story for My Shop.docx`. Please analyse it.

**Assistant:**

`[tool call] Skill(test-requirements-analysis)`
`[tool call] Read(skills/test-requirements-analysis/SKILL.md)`
`[tool call] Read(skills/test-requirements-analysis/references/tr-writing-rules.md)`

### Requirements analysis


#### 1. Facts (explicitly stated)

- Customer wants to submit a review for a product they purchased.
- Customers can enter a star rating.
- There is a text box for review comments.
- Approved reviews are displayed on the product page.
- From the mockup: Rating, Review, Name, and Email are marked required.
- Five star icons are visible.
- Email is stated as not published.
- A save-info checkbox and Submit button are visible.

#### 2. Assumptions (not stated, inferred)

- Five visible stars suggest a 1–5 whole-star scale, but this is not explicitly confirmed.
- “Approved reviews” suggests a moderation/pending state, but the workflow is not defined.
- Purchase eligibility may be enforced by the system, but the requirement does not say how.
- The save-info checkbox likely persists information in the browser, but scope/duration are not defined.

#### 3. Missing / ambiguous information

Main gaps found:

- How the system verifies the customer actually purchased the product.
- Exact rating scale, half-star support, default/unselected behavior.
- Review min/max length, allowed characters, whitespace, emoji/HTML handling.
- Exact validation messages and placement.
- Review approval process, statuses, and who approves.
- What happens immediately after Submit.
- Behavior of pending/rejected reviews.
- Public review fields, ordering, pagination.
- Email validation.
- Duplicate-review policy.
- Save-info persistence rules and why the label mentions Website while no Website field is visible.

#### 4. Risks & edge cases

- Positive: eligible customer submits a valid review; approved review appears on the correct product.
- Negative: missing required fields, invalid email, guest/non-purchaser, duplicate submission.
- Boundary: lowest/highest rating, empty/whitespace comment, long comment.
- Error handling: network/server failure; avoid false success or duplicate records.
- UI/Navigation: star-selection state, validation display, multiline/paste, checkbox behavior, Back/Refresh, keyboard accessibility.
- Integration/Regression: correct purchase/product mapping, existing reviews preserved, no cross-product review contamination.
- Security: XSS/script content must not execute; customer email remains private.

#### 5. Clarification questions


**Must ask**

- How does the system verify that the customer purchased the product, and what happens for a guest/non-purchaser?
- What rating values are allowed? Are half-stars supported?
- Who/what approves a review, and what statuses exist?
- What does the customer see immediately after Submit?
- Are pending/rejected reviews hidden from the product page?

**Nice to confirm**

- What are the review length and allowed-character rules?
- What email-validation rules should be used?
- Can the same customer submit multiple reviews for the same product?
- Which review fields are publicly displayed, and how are reviews ordered/paginated?
- How long does the save-info checkbox persist data?
- What accessibility behavior is expected for the star control?

`[tool call] Bash(python build_tr.py)`

```python
from pathlib import Path
import shutil
from openpyxl import load_workbook

BASE = Path('/mnt/data')
TEMPLATE = BASE / 'skills' / 'test-requirements-analysis' / 'assets' / 'Test_Requirement_Template.xlsx'
OUT = BASE / 'Test_Requirement_US-VP02.xlsx'
shutil.copy(TEMPLATE, OUT)
wb = load_workbook(OUT)
ws = wb['Test Requirement']

rows = [  # (AC ID, Acceptance Criteria, TR ID, Test Requirements, Notes)
    ('AC_01', 'Allow customers to enter a star rating', 'TR_001', 'The product review form provides a control that allows the customer to enter a star rating.', 'Fact — Acceptance Criteria 1.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_002', 'The star rating field is treated as required during review submission.', 'Fact — Mockup marks "Your rating" with * and states that required fields are marked *.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_003', 'The rating control presents five visible star icons to the user.', 'Fact — Mockup shows five star icons in the rating control.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_004', 'The rating scale is 1–5 whole stars.', 'Assumption — confirm with BA/PO: five visible stars suggest a 1–5 whole-star scale, but allowed values are not explicitly stated.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_005', 'Confirm the exact allowed rating values, whether half-star values are supported, and the default state before a rating is selected.', 'Missing info — Must ask: exact star-rating scale and selection rules are not defined.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_006', 'The lowest supported rating can be selected and remains selected before submission.', 'Edge case (boundary) — verify the lower boundary once the supported rating scale is confirmed.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_007', 'The highest supported rating can be selected and remains selected before submission.', 'Edge case (boundary) — verify the upper boundary once the supported rating scale is confirmed.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_008', 'Submitting the review without selecting a rating is rejected because the rating is marked as required.', 'Edge case (negative) — required-field behavior is visible in the mockup; exact validation message is still undefined.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_009', 'The selected star rating is visually clear and does not change unexpectedly before submission.', 'Risk (UI behavior) — prevent ambiguous or unstable star-selection state.'),
    ('AC_01', 'Allow customers to enter a star rating', 'TR_010', 'The star-rating control can be operated using the keyboard and its selected value can be understood by assistive technology.', 'Risk (accessibility) — rating widgets are often difficult to use without mouse input.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_011', 'The product review form provides a text box for review comments.', 'Fact — Acceptance Criteria 2.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_012', 'The review comment field is treated as required during review submission.', 'Fact — Mockup marks "Your review" with * and states that required fields are marked *.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_013', 'Confirm the minimum/maximum review length and the allowed characters, Unicode/emoji, and HTML handling.', 'Missing info — Nice to confirm: comment validation rules are not specified.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_014', 'Submitting the review with an empty review comment is rejected because the review field is marked as required.', 'Edge case (negative) — required-field behavior is visible in the mockup; exact validation message is still undefined.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_015', 'Confirm whether a review containing only spaces is treated as empty and whether leading/trailing spaces are trimmed.', 'Missing info — Nice to confirm: whitespace handling is not defined.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_016', 'Review comment content containing HTML or script-like text is displayed or rejected safely and is never executed as active script.', 'Risk (security) — protect the product page from stored script injection through review content.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_017', 'Very long review comments are handled according to the confirmed length rule without data corruption or broken page layout.', 'Edge case (boundary) — verify at the configured maximum and just beyond it once the limit is confirmed.'),
    ('AC_02', 'Provide a text box for review comments', 'TR_018', 'Multiline text and pasted review content are retained correctly through submission.', 'Risk (UI behavior) — the mockup uses a multiline text area.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_019', 'Approved reviews are displayed on the relevant product page.', 'Fact — Acceptance Criteria 3.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_020', 'A submitted review enters a moderation state before it becomes visible.', 'Assumption — confirm with BA/PO: the phrase "approved reviews" implies moderation, but the workflow is not defined.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_021', 'Confirm who or what approves reviews and which review statuses exist before a review becomes visible.', 'Missing info — Must ask: the approval workflow and approval actor are not defined.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_022', 'Confirm what the customer sees immediately after submitting a review, including the initial review status and any confirmation message or redirect.', 'Missing info — Must ask: the post-submit result and initial status are not defined.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_023', 'Confirm whether pending and rejected reviews are hidden from the product page and whether the customer can see their status elsewhere.', 'Missing info — Must ask: behavior for non-approved review states is not defined.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_024', 'An approved review appears on the same product page that the customer reviewed and does not appear on a different product.', 'Risk (integration/regression) — product-to-review mapping must remain correct.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_025', 'Existing approved reviews remain visible and unchanged when another review is approved.', 'Risk (integration/regression) — adding a new review must not remove or corrupt existing review data.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_026', 'Confirm which review fields are shown publicly and the display order/pagination rules when multiple approved reviews exist.', 'Missing info — Nice to confirm: approved-review presentation is not defined.'),
    ('AC_03', 'Display approved reviews on the product page', 'TR_027', 'The publicly displayed approved review reflects the approved rating and review content without unexpected changes.', 'Risk (UI behavior) — displayed review data should match the approved submission.'),
    ('N/A', '', 'TR_028', 'The review flow supports the stated user goal: a customer submits a review for a product the customer purchased.', 'Fact — User Story goal; no single Acceptance Criterion covers purchase eligibility.'),
    ('N/A', '', 'TR_029', 'The review form contains a Name field marked as required.', 'Fact — Mockup shows "Name *" and states that required fields are marked *.'),
    ('N/A', '', 'TR_030', 'The review form contains an Email field marked as required.', 'Fact — Mockup shows "Email *" and states that required fields are marked *.'),
    ('N/A', '', 'TR_031', 'The customer email address is not published with the review.', 'Fact — Mockup explicitly states "Your email address will not be published."'),
    ('N/A', '', 'TR_032', 'The review form contains a checkbox labeled to save the customer name, email, and website in the browser for the next comment.', 'Fact — Visible checkbox label in the mockup; no Website input is visible in the provided screen.'),
    ('N/A', '', 'TR_033', 'The review form provides a Submit button.', 'Fact — Submit button is visible in the mockup.'),
    ('N/A', '', 'TR_034', 'A guest or non-purchaser attempting to submit a review is handled according to the confirmed purchase-eligibility rule and cannot bypass any intended restriction.', 'Risk (negative/security) — validate authorization once the purchase-eligibility rule is confirmed.'),
    ('N/A', '', 'TR_035', 'Purchase eligibility is checked against the correct customer and the correct product/order history.', 'Risk (integration/regression) — incorrect purchase-history mapping could allow or block the wrong customer.'),
    ('N/A', '', 'TR_036', 'An invalid email address is handled according to the confirmed email-validation rule.', 'Risk (negative) — validate invalid-format behavior after the email rule is confirmed.'),
    ('N/A', '', 'TR_037', 'Repeated clicks on Submit do not create unintended duplicate reviews beyond the confirmed duplicate-review policy.', 'Risk (negative/error handling) — protect against accidental double submission.'),
    ('N/A', '', 'TR_038', 'A network or server failure during submission does not falsely show success and leaves the review state clear to the customer.', 'Risk (error handling) — failure behavior is not defined in the source requirement.'),
    ('N/A', '', 'TR_039', 'Refreshing or navigating Back after submission does not create an unintended duplicate review or an inconsistent submission state.', 'Risk (navigation) — verify browser navigation around form submission.'),
    ('N/A', '', 'TR_040', 'When the save-info checkbox is selected, persistence matches the confirmed rule; when it is not selected, the form does not persist those values beyond the allowed scope.', 'Risk (UI behavior/privacy) — checkbox behavior must match its label and the confirmed persistence rule.'),
    ('N/A', '', 'TR_041', 'The customer email remains non-public when an approved review is displayed.', 'Risk (security/privacy) — reinforce the explicit mockup statement across the published review flow.'),
    ('N/A', '', 'TR_042', 'Name and review text are handled safely so user-supplied markup or script cannot execute on the product page.', 'Risk (security) — protect public review rendering from stored injection.'),
    ('N/A', '', 'TR_043', 'Required-field errors are shown consistently and identify the field that needs correction.', 'Risk (UI behavior) — validation feedback should be understandable and actionable.'),
    ('N/A', '', 'TR_044', 'Required form fields and the Submit action are reachable and understandable using keyboard navigation and accessible labels.', 'Risk (accessibility) — review submission should remain usable without pointer-only interaction.'),
    ('N/A', '', 'TR_045', 'Submitting or approving a review for one product does not change review data on unrelated products.', 'Risk (integration/regression) — prevent cross-product review contamination.'),
    ('N/A', '', 'TR_046', 'Confirm how the system verifies that the customer purchased the product and what should happen for a guest or a customer who did not purchase it.', 'Missing info — Must ask: purchase eligibility is part of the user-story context but enforcement and failure behavior are not defined.'),
    ('N/A', '', 'TR_047', 'Confirm the accepted email format and the expected validation behavior for an invalid email address.', 'Missing info — Nice to confirm: email validation rules and error behavior are not specified.'),
    ('N/A', '', 'TR_048', 'Confirm whether the same customer can submit more than one review for the same product and what counts as a duplicate.', 'Missing info — Nice to confirm: duplicate-review policy is not defined.'),
    ('N/A', '', 'TR_049', 'Confirm how long and where the "save my name, email, and website" checkbox persists data, and why the label mentions Website although no Website input is visible.', 'Missing info — Nice to confirm: persistence scope/duration and the Website-field mismatch are not defined.'),
    ('N/A', '', 'TR_050', 'Confirm the exact wording and placement of validation messages for missing or invalid required fields.', 'Missing info — Nice to confirm: error message text and placement are not specified.'),
]
for i, row in enumerate(rows, start=5):
    for c, v in enumerate(row, start=1):
        ws.cell(i, c, v)
wb.save(OUT)
print(len(rows), 'TR rows written to', OUT.name)

```

Created `Test_Requirement_US-VP02.xlsx` by copying the template.

---

## Turn 2: test cases

**User:** Now generate the test cases from the TR list.

**Assistant:**

`[tool call] Skill(test-case-generation)`
`[tool call] Read(skills/test-case-generation/SKILL.md)`
`[tool call] Read(skills/test-case-generation/references/tc-writing-rules.md)`
`[tool call] Bash(python build_tc.py)`

```python
from pathlib import Path
import shutil, math, re
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Side

BASE = Path('/mnt/data')
SKILL_DIR = BASE / 'tc_skill_unpack' / '2. test-case-generation'
TR_FILE = BASE / 'Test_Requirement_US-VP02.xlsx'
OUT = BASE / 'Test_Case_US-VP02.xlsx'
TEMPLATE = SKILL_DIR / 'assets' / 'Test_Case_Template.xlsx'

# Direct input to the skill is the TR list previously generated from the same US-VP02 Word story.
# The Word US/mockup remains the source for visible labels and user-story context.
tr_wb = load_workbook(TR_FILE, data_only=True)
tr_ws = tr_wb['Test Requirement']
trs = {}
for r in range(5, tr_ws.max_row + 1):
tr_id = tr_ws.cell(r, 3).value
if tr_id:
trs[tr_id] = {
'ac_id': tr_ws.cell(r, 1).value,
'ac': tr_ws.cell(r, 2).value,
'req': tr_ws.cell(r, 4).value,
'notes': tr_ws.cell(r, 5).value or '',
}

rows = []
def add(tr, summary, pre, steps, expected, type_, priority, extra=None, blocked_reason=None):
assert tr in trs, f'Unknown TR {tr}'
tc = f"TC_{len(rows)+1:03d}"
src_note = trs[tr]['notes']
if blocked_reason:
notes = f"BLOCKED — pending clarification: {blocked_reason} | Type: {type_} | Priority: {priority}"
else:
notes = f"Type: {type_} | Priority: {priority}"
# Carry forward flags/categories from TR Notes.
if src_note.startswith('Assumption —'):
notes += ' | ' + src_note
elif src_note.startswith('Risk (') or src_note.startswith('Edge case ('):
notes += ' | ' + src_note
elif src_note.startswith('Missing info — Nice to confirm:'):
notes += ' | ' + src_note
elif src_note.startswith('Missing info — Must ask:') and not blocked_reason:
raise AssertionError(f'{tr} is Must ask but not BLOCKED')
if extra:
notes += ' | ' + extra
rows.append((tr, tc, summary, pre, steps, expected, notes))

COMMON_PRE = 'Product detail page for a product available for review is open.'
PURCHASED_PRE = 'Customer "reviewer01@example.com" is signed in and has purchased Product A. Product A review form is open.'

# AC_01 — Rating
add('TR_001','Select a star rating on the review form',COMMON_PRE,
'1. Locate the "Your rating" control.\n2. Click the fourth visible star.',
'The rating control shows the fourth star selection as the current rating.', 'Positive','High')
add('TR_002','Reject submission when rating is not selected',COMMON_PRE,
'1. Leave "Your rating" unselected.\n2. Enter "Great product and comfortable fit." in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'The review is not submitted, and validation identifies "Your rating" as a required field.', 'Negative','Medium')
add('TR_003','Display five star icons in the rating control',COMMON_PRE,
'1. Locate the "Your rating" control.\n2. Count the visible star icons.',
'Exactly five star icons are visible in the rating control.', 'UI','Low')
add('TR_004','Select a whole-star rating using the visible five-star control',COMMON_PRE,
'1. Click the third visible star in "Your rating".\n2. Click outside the rating control without submitting.',
'The third whole-star position remains selected before submission.', 'Positive','Medium')
add('TR_005','Confirm supported rating values and default selection behavior',COMMON_PRE,
'1. Review the product requirement with BA/PO.\n2. Record the allowed rating values, whether half-stars are supported, and the default unselected state.',
'TBD — confirm the exact rating scale, half-star support, and default state before executing rating-value tests.', 'Requirement Clarification','High',
blocked_reason='exact star-rating scale and selection rules are not defined')
add('TR_006','Select the lowest visible rating boundary',COMMON_PRE,
'1. Click the leftmost visible star in "Your rating".\n2. Move focus to the "Your review" field.',
'The leftmost star remains selected as the current rating until the user changes it or submits the form.', 'Boundary','Medium')
add('TR_007','Select the highest visible rating boundary',COMMON_PRE,
'1. Click the rightmost visible star in "Your rating".\n2. Move focus to the "Your review" field.',
'The rightmost star remains selected as the current rating until the user changes it or submits the form.', 'Boundary','Medium')
add('TR_008','Reject review submission with no rating',COMMON_PRE,
'1. Leave "Your rating" unselected.\n2. Enter "Good quality." in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'The form remains unsubmitted and shows a validation indication for the required rating field.', 'Negative','Medium')
add('TR_009','Keep the latest star selection stable before submission',COMMON_PRE,
'1. Click the second visible star.\n2. Click the fourth visible star.\n3. Click inside the "Your review" text box.',
'The fourth star remains the selected rating; the earlier second-star selection is no longer shown as current.', 'UI','Medium')
add('TR_010','Operate the rating control by keyboard and expose its selected state',COMMON_PRE,
'1. Use Tab from the top of the review form until the rating control receives keyboard focus.\n2. Use the keyboard interaction exposed by the rating widget to select a rating.\n3. Inspect the control with the browser accessibility tree or a screen reader.',
'The rating can be selected without a mouse, and the selected value/state is exposed to assistive technology.', 'Accessibility','Medium')

# AC_02 — Review comment
add('TR_011','Display a review comment text box',COMMON_PRE,
'1. Locate the field labeled "Your review".\n2. Click inside the field.\n3. Type "Great product and comfortable fit.".',
'A multiline review text box is present and accepts the entered review text.', 'UI','High')
add('TR_012','Reject submission when review comment is empty',COMMON_PRE,
'1. Select the fourth star.\n2. Leave "Your review" empty.\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'The review is not submitted, and validation identifies "Your review" as a required field.', 'Negative','Medium')
add('TR_013','Confirm review comment validation rules',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record minimum length, maximum length, allowed characters, Unicode/emoji handling, and HTML handling.',
'TBD — confirm the review comment validation rules before executing length/character boundary cases.', 'Requirement Clarification','Low')
add('TR_014','Reject submission with an empty review comment',COMMON_PRE,
'1. Select the third star.\n2. Leave "Your review" empty.\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'The form remains unsubmitted and shows a validation indication for the required review field.', 'Negative','Medium')
add('TR_015','Determine behavior for a whitespace-only review comment',COMMON_PRE,
'1. Select the third star.\n2. Enter five space characters in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'TBD — confirm whether whitespace-only review text is treated as empty and whether leading/trailing spaces are trimmed.', 'Boundary','Low')
add('TR_016','Prevent script execution from review content',COMMON_PRE,
'1. Select the fourth star.\n2. Enter "<script>alert(1)</script>" in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Submit the review using the normal flow.\n6. If the review becomes approved, open the product page that displays it.',
'The supplied script-like text is rejected or rendered as inert text; no script executes in the browser.', 'Security','High')
add('TR_017','Validate review comment at the configured maximum boundary',COMMON_PRE,
'1. Obtain the confirmed maximum review length from the requirement.\n2. Prepare one comment exactly at that maximum and one comment one character longer.\n3. Submit each value with all other required fields populated.',
'TBD — at the configured maximum the behavior follows the confirmed rule, and the value one character over is handled according to the confirmed validation rule without data corruption or broken layout.', 'Boundary','Medium',
blocked_reason='maximum review length is not defined')
add('TR_018','Retain multiline and pasted review text through submission',PURCHASED_PRE,
'1. Select the fourth star.\n2. Paste this text into "Your review": "Line 1: Great fit.\nLine 2: Comfortable fabric."\n3. Enter "QA Tester" in "Name".\n4. Enter "reviewer01@example.com" in "Email".\n5. Click "Submit".',
'The submitted review retains both text lines and their content without truncation or unexpected character changes.', 'UI','Medium')

# AC_03 — Approved reviews
add('TR_019','Display an approved review on the relevant product page','An approved review exists for Product A with rating 4 and comment "Great product and comfortable fit.".',
'1. Open Product A detail page.\n2. Scroll to the reviews section.',
'The approved Product A review is visible on Product A detail page.', 'Positive','High')
add('TR_020','Place a newly submitted review into moderation before public display',PURCHASED_PRE,
'1. Select the fourth star.\n2. Enter "Waiting for approval test." in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "reviewer01@example.com" in "Email".\n5. Click "Submit".\n6. Reopen Product A public review section.',
'The new review is not treated as publicly approved immediately; it remains in a moderation state before public display.', 'Workflow','Medium')
add('TR_021','Confirm review approval actor and status model',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record who or what approves reviews.\n3. Record all statuses between submission and public display.',
'TBD — confirm the approval actor and review statuses before executing approval-workflow tests.', 'Requirement Clarification','High',
blocked_reason='approval workflow and approval actor are not defined')
add('TR_022','Confirm the customer-visible result immediately after Submit',PURCHASED_PRE,
'1. Review the requirement with BA/PO.\n2. Record the expected confirmation message, redirect/page state, and initial review status after successful submission.',
'TBD — confirm the post-submit message/page behavior and initial review status.', 'Requirement Clarification','High',
blocked_reason='post-submit result and initial status are not defined')
add('TR_023','Confirm visibility rules for pending and rejected reviews',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record whether pending reviews are publicly visible.\n3. Record whether rejected reviews are publicly visible.\n4. Record whether customers can view their own review status elsewhere.',
'TBD — confirm visibility and customer-status behavior for pending and rejected reviews.', 'Requirement Clarification','High',
blocked_reason='behavior for non-approved review states is not defined')
add('TR_024','Keep an approved review mapped to the correct product','Approved review R-A belongs to Product A; Product B is a different product.',
'1. Open Product A detail page and locate review R-A.\n2. Open Product B detail page.\n3. Search Product B reviews for the text from R-A.',
'Review R-A is visible on Product A and is not displayed on Product B.', 'Integration','High')
add('TR_025','Preserve existing approved reviews when another review is approved','Product A already has approved review R-OLD. A second review R-NEW is ready to be approved.',
'1. Record the visible text and rating of R-OLD on Product A.\n2. Approve R-NEW using the project review-approval mechanism.\n3. Reload Product A reviews.',
'R-NEW appears as approved, and R-OLD remains visible with its original rating and review text unchanged.', 'Regression','High')
add('TR_026','Confirm public review fields, ordering, and pagination rules','Product A has multiple approved reviews available for display.',
'1. Review the requirement with BA/PO.\n2. Record which review fields are public.\n3. Record sorting/order rules.\n4. Record pagination or load-more behavior.',
'TBD — confirm the public review fields, ordering rule, and pagination behavior before validating presentation details.', 'Requirement Clarification','Low')
add('TR_027','Display the approved rating and review text without modification','Approved review R1 has rating 4 and text "Great product and comfortable fit." for Product A.',
'1. Open Product A detail page.\n2. Locate approved review R1.\n3. Compare the displayed rating and text with R1 source values.',
'R1 displays rating 4 and the text "Great product and comfortable fit." without unexpected content changes.', 'UI','Medium')

# N/A facts / cross-cutting
add('TR_028','Submit a review for a product the customer purchased',PURCHASED_PRE,
'1. Select the fourth star.\n2. Enter "Great product and comfortable fit." in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "reviewer01@example.com" in "Email".\n5. Click "Submit".',
'The review submission is accepted into the review workflow for Product A without a required-field validation error.', 'Positive','High')
add('TR_029','Display the required Name field',COMMON_PRE,
'1. Locate the "Name" field.\n2. Verify the required indicator shown with the field.',
'A field labeled "Name" is visible and is marked as required.', 'UI','Medium')
add('TR_029','Reject submission when Name is empty',COMMON_PRE,
'1. Select the fourth star.\n2. Enter "Great product." in "Your review".\n3. Leave "Name" empty.\n4. Enter "qa.tester@example.com" in "Email".\n5. Click "Submit".',
'The review is not submitted, and validation identifies "Name" as a required field.', 'Negative','Medium')
add('TR_030','Display the required Email field',COMMON_PRE,
'1. Locate the "Email" field.\n2. Verify the required indicator shown with the field.',
'A field labeled "Email" is visible and is marked as required.', 'UI','Medium')
add('TR_030','Reject submission when Email is empty',COMMON_PRE,
'1. Select the fourth star.\n2. Enter "Great product." in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Leave "Email" empty.\n5. Click "Submit".',
'The review is not submitted, and validation identifies "Email" as a required field.', 'Negative','Medium')
add('TR_031','Keep reviewer email private on an approved review','Approved review R1 was submitted with email "private.reviewer@example.com".',
'1. Open the product page containing approved review R1.\n2. Inspect the public review content and reviewer information.',
'The email address "private.reviewer@example.com" is not displayed in the public review.', 'Security','High')
add('TR_032','Display the save-info checkbox and its visible label',COMMON_PRE,
'1. Locate the checkbox below the Email field.\n2. Read the checkbox label.\n3. Inspect the visible form fields.',
'A checkbox is visible with the label about saving name, email, and website in the browser for the next comment; no separate Website input is visible in the provided form layout.', 'UI','Low')
add('TR_033','Display the Submit button',COMMON_PRE,
'1. Scroll to the bottom of the review form.\n2. Locate the button labeled "Submit".',
'A visible button labeled "Submit" is present on the review form.', 'UI','High')
add('TR_034','Confirm purchase-eligibility enforcement and failure behavior',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record how purchase ownership is verified.\n3. Record expected behavior for a guest.\n4. Record expected behavior for a signed-in customer who did not purchase the product.',
'TBD — confirm purchase verification and the expected guest/non-purchaser behavior before executing authorization tests.', 'Requirement Clarification','High',
blocked_reason='purchase eligibility enforcement and failure behavior are not defined')
add('TR_035','Prevent a guest from bypassing purchase-eligibility restrictions','Guest session; Product A review form is reachable.',
'1. Open Product A as a guest.\n2. Select the fourth star.\n3. Enter "Guest attempt" in "Your review".\n4. Enter "Guest Tester" in "Name".\n5. Enter "guest@example.com" in "Email".\n6. Click "Submit".',
'TBD — the guest attempt is handled according to the confirmed purchase-eligibility rule and must not bypass an intended purchaser-only restriction.', 'Negative/Security','High',
blocked_reason='guest behavior under purchase eligibility is not defined')
add('TR_035','Prevent a signed-in non-purchaser from bypassing purchase-eligibility restrictions','Customer "nonbuyer@example.com" is signed in and has not purchased Product A.',
'1. Open Product A review form.\n2. Select the fourth star.\n3. Enter "Non-purchaser attempt" in "Your review".\n4. Enter "Non Buyer" in "Name".\n5. Enter "nonbuyer@example.com" in "Email".\n6. Click "Submit".',
'TBD — the non-purchaser attempt is handled according to the confirmed purchase-eligibility rule and must not bypass an intended purchaser-only restriction.', 'Negative/Security','High',
blocked_reason='non-purchaser behavior under purchase eligibility is not defined')
add('TR_036','Check purchase eligibility against the correct customer and product','Customer A purchased Product A but did not purchase Product B; Customer B purchased Product B.',
'1. Sign in as Customer A and open Product A review form.\n2. Check the review eligibility state.\n3. Open Product B review form as Customer A and check the eligibility state.\n4. Sign in as Customer B and open Product B review form.\n5. Compare the three eligibility results.',
'Eligibility is evaluated using the current customer plus the current product/order history; Product A purchase status does not incorrectly grant Product B eligibility, and Customer B is evaluated using Customer B history.', 'Integration','High')
add('TR_037','Confirm accepted email format and invalid-email validation',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record the accepted email format.\n3. Record validation message/behavior for an invalid email address.',
'TBD — confirm email validation rules and invalid-email behavior before executing format-specific tests.', 'Requirement Clarification','Low')
add('TR_038','Handle an invalid email according to the confirmed validation rule',COMMON_PRE,
'1. Select the fourth star.\n2. Enter "Email validation test" in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "invalid-email" in "Email".\n5. Click "Submit".',
'TBD — after the email rule is confirmed, the malformed value "invalid-email" is handled according to that validation rule and is not silently accepted when it violates the confirmed format.', 'Negative','Medium',
blocked_reason='email validation rule is not defined')
add('TR_039','Confirm duplicate-review policy for the same customer and product',PURCHASED_PRE,
'1. Review the requirement with BA/PO.\n2. Record whether multiple reviews are allowed for the same customer/product.\n3. Record what fields or state define a duplicate.',
'TBD — confirm the duplicate-review policy before executing repeated-submission cases.', 'Requirement Clarification','Low')
add('TR_040','Prevent unintended duplicate reviews from rapid double-submit',PURCHASED_PRE,
'1. Select the fourth star.\n2. Enter "Double submit test" in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "reviewer01@example.com" in "Email".\n5. Double-click "Submit" rapidly.\n6. Inspect the created review records or resulting review state.',
'The rapid double-click does not create unintended duplicate review records beyond what the confirmed duplicate-review policy allows.', 'Negative/Error Handling','High')
add('TR_041','Keep review state clear when network is lost during Submit',PURCHASED_PRE,
'1. Select the fourth star.\n2. Enter "Network failure test" in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "reviewer01@example.com" in "Email".\n5. Disable the network immediately before clicking "Submit".\n6. Click "Submit".',
'The UI does not falsely indicate that the review was successfully submitted; the customer can tell the submission did not complete.', 'Error Handling','High')
add('TR_041','Keep review state clear when the server returns an error',PURCHASED_PRE,
'1. Prepare the test environment so the review-submit request returns a server error.\n2. Select the fourth star.\n3. Enter "Server failure test" in "Your review".\n4. Enter "QA Tester" in "Name" and "reviewer01@example.com" in "Email".\n5. Click "Submit".',
'The UI does not falsely indicate success, and the review state remains clearly unsuccessful/pending retry rather than appearing approved or submitted.', 'Error Handling','High')
add('TR_042','Do not create a duplicate review after browser Refresh','A review submission for Product A has just completed once in the test environment.',
'1. Note the number of review records created by the submission.\n2. Refresh the browser page.\n3. Recheck review records/status for the same submission.',
'Refreshing the page does not create an additional review record or change the completed submission into an inconsistent state.', 'Navigation','Medium')
add('TR_042','Do not create a duplicate review after using browser Back','A review submission for Product A has just completed once in the test environment.',
'1. Note the number of review records created by the submission.\n2. Use the browser Back button.\n3. Navigate forward/open Product A again.\n4. Recheck review records/status.',
'Using Back and returning to the product does not create an additional review record or corrupt the original submission state.', 'Navigation','Medium')
add('TR_043','Confirm save-info persistence scope and Website-label mismatch',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record where the saved name/email data is stored and for how long.\n3. Confirm whether a Website field should exist or whether the checkbox label should omit Website.',
'TBD — confirm persistence scope/duration and the intended Website-field behavior/label.', 'Requirement Clarification','Low')
add('TR_044','Persist saved review identity according to the confirmed checkbox rule',COMMON_PRE,
'1. Check the save-info checkbox.\n2. Enter "QA Saved" in "Name" and "saved@example.com" in "Email".\n3. Complete a review submission.\n4. Reopen the review form within the confirmed persistence scope.',
'TBD — with the checkbox selected, the Name/Email values persist only as allowed by the confirmed persistence rule.', 'UI/Privacy','Medium',
blocked_reason='save-info persistence scope and duration are not defined')
add('TR_044','Do not persist review identity when the save-info checkbox is not selected',COMMON_PRE,
'1. Leave the save-info checkbox cleared.\n2. Enter "QA Not Saved" in "Name" and "notsaved@example.com" in "Email".\n3. Complete a review submission.\n4. Reopen the review form within the confirmed persistence scope.',
'TBD — with the checkbox not selected, the Name/Email values are not persisted beyond the scope allowed by the confirmed rule.', 'UI/Privacy','Medium',
blocked_reason='save-info persistence scope and duration are not defined')
add('TR_045','Keep customer email private after review approval','Approved review R-PRIVATE was submitted with email "secret@example.com".',
'1. Open the public product page containing R-PRIVATE.\n2. Inspect the review text, metadata, and visible reviewer information.\n3. Search the rendered page for "secret@example.com".',
'The email address "secret@example.com" is not displayed as part of the public approved review.', 'Security/Privacy','High')
add('TR_046','Prevent script execution from reviewer Name','Product A review form is open.',
'1. Select the fourth star.\n2. Enter "Safe review text" in "Your review".\n3. Enter "<img src=x onerror=alert(1)>" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Submit and, if approved, open the public review.',
'The supplied markup in Name is rejected or rendered inert; no script/event handler executes on the public product page.', 'Security','High')
add('TR_046','Prevent script execution from review text on public display','Product A review form is open.',
'1. Select the fourth star.\n2. Enter "<svg onload=alert(1)>" in "Your review".\n3. Enter "QA Tester" in "Name".\n4. Enter "qa.tester@example.com" in "Email".\n5. Submit and, if approved, open the public review.',
'The supplied markup in review text is rejected or rendered inert; no script/event handler executes on the public product page.', 'Security','High')
add('TR_047','Confirm exact validation message wording and placement',COMMON_PRE,
'1. Review the requirement with BA/PO.\n2. Record exact text and placement for missing-rating, missing-review, missing-name, missing-email, and invalid-email validation.',
'TBD — confirm validation wording and placement before asserting exact messages in test execution.', 'Requirement Clarification','Low')
add('TR_048','Show consistent required-field feedback for all missing required inputs',COMMON_PRE,
'1. Leave "Your rating", "Your review", "Name", and "Email" empty.\n2. Click "Submit".',
'The form is not submitted, and validation feedback identifies each required field that needs correction: rating, review, Name, and Email.', 'UI/Negative','Medium')
add('TR_049','Navigate all required review controls and Submit by keyboard',COMMON_PRE,
'1. Place keyboard focus at the start of the review form.\n2. Use Tab/Shift+Tab to move through rating, review, Name, Email, save-info checkbox, and Submit.\n3. Activate "Submit" using the keyboard after entering test values.',
'Each required control and the Submit action can receive keyboard focus in a usable order and can be operated without pointer-only interaction.', 'Accessibility','Medium')
add('TR_049','Expose understandable accessible labels for review fields and Submit',COMMON_PRE,
'1. Inspect rating, review, Name, Email, checkbox, and Submit using the browser accessibility tree or a screen reader.\n2. Check the accessible name/role/state of each control.',
'Each control exposes an understandable accessible name and appropriate role/state so a keyboard/screen-reader user can identify its purpose.', 'Accessibility','Medium')
add('TR_050','Keep review data isolated between unrelated products','Product A and Product B are different products. Product A has review R-A ready for submission/approval. Record Product B existing review list before the test.',
'1. Submit and approve R-A for Product A using the project workflow.\n2. Open Product A and confirm R-A is present.\n3. Open Product B and compare its review list with the recorded pre-test state.',
'R-A is associated with Product A only, and Product B review data remains unchanged from its pre-test state.', 'Integration/Regression','High')

# Validation against source TR list and skill rules
tr_ids = set(trs)
covered = {r[0] for r in rows}
missing = sorted(tr_ids - covered)
extra = sorted(covered - tr_ids)
assert not missing, f'Missing TR coverage: {missing}'
assert not extra, f'Unknown TRs in output: {extra}'
assert len({r[1] for r in rows}) == len(rows), 'TC IDs not unique'
assert [r[1] for r in rows] == [f'TC_{i:03d}' for i in range(1, len(rows)+1)]

must_ask = {tr for tr, d in trs.items() if d['notes'].startswith('Missing info — Must ask:')}
for tr in must_ask:
cases = [r for r in rows if r[0] == tr]
assert cases, tr
for r in cases:
assert r[5].startswith('TBD —'), f'{r[1]} expected must start TBD'
assert r[6].startswith('BLOCKED —'), f'{r[1]} notes must start BLOCKED'

flagged = {tr for tr,d in trs.items() if d['notes'].startswith(('Edge case (','Risk (','Assumption —'))}
for tr in flagged:
assert any(r[0] == tr for r in rows), f'Flagged TR lacks dedicated TC: {tr}'

forbidden = ['works correctly','works properly','as expected','displayed correctly']
for r in rows:
exp = r[5].lower().strip()
for phrase in forbidden:
assert exp != phrase, f'Forbidden vague expected in {r[1]}'
assert '\n' in r[4] or r[4].startswith('1.'), f'Steps not numbered in {r[1]}'

# Copy the exact skill asset template, then fill only data rows.
shutil.copy(TEMPLATE, OUT)
wb = load_workbook(OUT)
ws = wb['TC List']
thin = Side(style='thin')
border = Border(left=thin, right=thin, top=thin, bottom=thin)
center = Alignment(horizontal='center', vertical='top')
wrap = Alignment(vertical='top', wrap_text=True)

for rr, values in enumerate(rows, start=5):
for col, val in enumerate(values, start=1):
cell = ws.cell(row=rr, column=col, value=val)
cell.alignment = center if col in (1,2) else wrap
cell.border = border
# Give multiline cells enough room while preserving template widths/styles.
max_lines = 1
for val in values[2:]:
text = str(val or '')
explicit = text.count('\n') + 1
# rough wrap estimate based on column widths; primarily protects Steps/Expected/Notes
est = max(explicit, math.ceil(len(text)/55))
max_lines = max(max_lines, est)
ws.row_dimensions[rr].height = min(15 * max_lines + 6, 150)

# Preserve exact title/header/template dimensions. Freeze not added because asset does not define it.
wb.save(OUT)

print(f'Created: {OUT}')
print(f'Total TRs: {len(tr_ids)}')
print(f'Total TCs: {len(rows)}')
print(f'Must-ask TRs: {len(must_ask)}; all BLOCKED/TBD')
print(f'Flagged assumption/risk/edge TRs: {len(flagged)}; all covered')
```

Created `Test_Case_US-VP02.xlsx`: every TR ID has at least one test case; the Must-ask TRs are BLOCKED.
