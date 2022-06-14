from dates import getToday, getDay


def test_today():
    # This will obviously fail if you run it after 2022-06-14, so it's not
    # a very useful test! It was just a very first example.
    assert getToday() == '2022-06-14'


def test_day():
    assert getDay('2022-06-14') == '14'
