import calendar
from datetime import datetime, date


def get_time():
    time = datetime.now().strftime("%I:%M %p")
    return f"The time is {time}"


def get_date():
    return f"The date is {str(date.today())}"


def get_day():
    return f"Today is {calendar.day_name[date.today().weekday()]}"
