import pandas as pd
import re

def clean_email(email):
    email = str(email).strip().lower()
    email = re.sub(r'\s+', '', email)
    return email

# NEW file (golden model)
new_df = pd.read_csv(
    "/Users/dimitricromarty/Downloads/SA CEA Student Listing Spring 2026.csv",
    encoding="latin1"
)

# OLD file
old_df = pd.read_excel(
    "/Users/dimitricromarty/Downloads/SA General_Student_Listing.xlsx"
)

# Adjust column names if needed
new_emails = set(
    clean_email(email)
    for email in new_df["All Institutional Email Addresses"].dropna()
)

old_emails = set(
    clean_email(email)
    for email in old_df["All Institutional Email Addresses"].dropna()
)

# What was added?
added = new_emails - old_emails

# What was removed?
removed = old_emails - new_emails

print(f"\n Added in new file: {len(added)}")
for email in added:
    print(email)

print(f"\n Removed from new file: {len(removed)}")
for email in removed:
    print(email)
