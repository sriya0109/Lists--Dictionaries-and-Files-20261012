"""
RECORD CHECK  -  my version
===========================

Name  :Sriya
Lane  :  AI       (delete two)
Date  :18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 
"""
RECORD CHECK - my version

Name: Sriya
Lane: AI and Data Science
Date: 18/10/2026
"""

# ===================================================================

def check_record(value, limit):
    """Calculate the difference, percentage and status for a record."""
    difference = value - limit

    if limit != 0:
        percent = (value / limit) * 100
    else:
        percent = 0.0

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label=None, value=None, limit=None,
                 difference=None, percent=None, status=None,
                 over_limit_count=None):
    """Print a record report or the final over-limit summary."""

    if over_limit_count is not None:
        print(f"Total records over limit: {over_limit_count}")
        return

    print(f"Label: {label}")
    print(f"Value: {value:.1f}")
    print(f"Limit: {limit:.1f}")
    print(f"Difference: {difference:.1f}")
    print(f"Percentage of limit: {percent:.1f}%")
    print(f"Status: {status}")
    print("-" * 30)



records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 50.0},
    {"label": "R-004", "value": 110.0, "limit": 100.0}
]

# 3. PROCESS + OUTPUT

over_limit_count = 0

with open("results.txt", "w") as output_file:

    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        # Print the report
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        # Count records over the limit
        if status == "OVER LIMIT":
            over_limit_count += 1

        # Save the label and status to the output file
        output_file.write(
            f"{record['label']}, {status}\n"
        )

# Printing the final count by using print_report
print_report(over_limit_count=over_limit_count)

print("Results saved to results.txt")
