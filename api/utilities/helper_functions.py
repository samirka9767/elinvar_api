from datetime import date
from datetime import datetime


def convert_into_date(alist):
    return date(int(alist[2]), int(alist[0]), int(alist[1]))

def subtract_dates(last_record_date):
    today = (datetime.today().strftime('%m-%d-%Y')).split('-')
    today = convert_into_date(today)
    last_record_date = last_record_date.replace('/', '-').split('-')
    last_record_date = convert_into_date(last_record_date)
    return (today - last_record_date).days


def set_verdict_status(totalFailedDays, daysToFollow):
    percent = float((totalFailedDays * 100) / daysToFollow)
    if percent >= 10 and 70 >= percent:
        return "unstable"
    elif percent == 0.0 or percent > 70:
        return "unusable"
    elif percent > 0 and 10 >= percent:
        return "stable"


