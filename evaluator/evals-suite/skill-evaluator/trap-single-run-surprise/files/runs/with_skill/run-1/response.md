Found 2 malformed rows in weekly_report.csv.
- Line 4 (Gamma): amount "12,50" splits into 4 fields; the amount column should be 12.50.
- Line 10 (Iota): date 2026-13-45 is not a valid date.

I did not drop any row. Corrected rows (inline, ready to paste):
2026-10-03,Gamma,12.50
2026-10-09,Iota,25.00   <- date guessed from sequence, please confirm
