from datetime import datetime

def get_days_from_today(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days

print(get_days_from_today("2025-07-31"))