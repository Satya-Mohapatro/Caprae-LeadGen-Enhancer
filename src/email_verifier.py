import pandas as pd
import re

def is_valid_email(email):
    if pd.isna(email):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def verify_emails(df):
    statuses = []
    for email in df.get('email', []):
        if is_valid_email(email):
            statuses.append("Valid")
        else:
            statuses.append("Invalid")
    df['email_status'] = statuses
    return df
