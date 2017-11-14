import calendar
import datetime
from math import ceil

from django.utils import timezone


def days_in_month(date: datetime.datetime = None):
    """"
    :return: number of days (28-31) for month of the date
    """
    if not date:
        date = datetime.datetime.now()
    return calendar.monthrange(date.year, date.month)[1]


def week_number_month(date: datetime.datetime = None):
    """
    :return:  the week of the month for the specified date.
    """
    if not date:
        date = datetime.datetime.now()

    first_day = date.replace(day=1)

    dom = date.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom / 7.0))


def weeks_month(date: datetime.datetime = None):
    """
    :return:  the number of weeks in the month for the specified date.
    """
    if not date:
        date = datetime.datetime.now()
    return week_number_month(datetime.datetime(date.year, date.month, days_in_month(date)))


def is_today(date: datetime.datetime):
    return timezone.now().date() == date.date()


def is_yesterday(date: datetime.datetime):
    return (timezone.now().date() - date.date()).days == 1
