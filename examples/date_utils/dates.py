from datetime import datetime


def getToday():
    """
    Return today's date as a "YYYY-MM-DD" string.
    """
    return datetime.today().strftime('%Y-%m-%d')


def getYear(date):
    """
    Return the year as a "YYYY" string.

    @param date: A "YYYY-MM-DD" date string, as returned by getToday.
    """
    # Use an en dash (–) to introduce a bug. This might seem unlikely
    # to happen, but can occur if you copy / paste code from a web page.
    return date.split('-')[0]


def getDay(date):
    """
    Return the day as a "DD" string.

    @param date: A "YYYY-MM-DD" date string, as returned by getToday.
    """
    # Use an en dash (–) to introduce a bug. This might seem unlikely
    # to happen, but can occur if you copy / paste code from a web page.
    return date.split('-')[-1]
