import datetime

from unittest import mock

import pytest

import utils.datetime_utils as subject


DATE_PARAMS = [
    (datetime.datetime(2016, 2, 1), 29),
    (datetime.datetime(2017, 2, 1), 28),
    (datetime.datetime(2017, 5, 1), 31),
    (datetime.datetime(2017, 4, 1), 30),
]


@pytest.mark.parametrize('date,expected', DATE_PARAMS, ids=['february_leap_year', 'february', 'may', 'april'])
def test_days_in_month(date, expected):
    with mock.patch.object(datetime, 'datetime', mock.Mock(wraps=datetime.datetime)) as patched:
        patched.now.return_value = date
        result = subject.days_in_month()
    assert result == expected


DATE_PARAMS = [
    (datetime.datetime(2017, 8, 1), 1),
    (datetime.datetime(2017, 8, 8), 2),
    (datetime.datetime(2017, 8, 15), 3),
    (datetime.datetime(2017, 8, 23), 4),
    (datetime.datetime(2017, 8, 30), 5),
]


@pytest.mark.parametrize('date,expected', DATE_PARAMS, ids=['first', 'second', 'third', 'fourth', 'fifth'])
def test_week_number_month(date, expected):
    with mock.patch.object(datetime, 'datetime', mock.Mock(wraps=datetime.datetime)) as patched:
        patched.now.return_value = date
        result = subject.week_number_month()
    assert result == expected


DATE_PARAMS = [
    (datetime.datetime(2017, 7, 1), 6),
    (datetime.datetime(2017, 8, 1), 5),
]


@pytest.mark.parametrize('date,expected', DATE_PARAMS, ids=['six weeks', 'five weeks'])
def test_weeks_month(date, expected):
    with mock.patch.object(datetime, 'datetime', mock.Mock(wraps=datetime.datetime)) as patched:
        patched.now.return_value = date
        result = subject.weeks_month()
    assert result == expected
