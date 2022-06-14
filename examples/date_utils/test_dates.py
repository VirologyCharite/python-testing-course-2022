from dates import getToday, getDay, getYear


def test_3_fields():
    assert len(getToday().split('-')) == 3


def test_length_10():
    assert len(getToday()) == 10


def test_year_2000():
    assert getYear('2020-05-17') == '2020'


def test_day_09():
    assert getDay('2022-06-09') == '09'


def test_day_9():
    assert getDay('2022-9-09') == '09'
