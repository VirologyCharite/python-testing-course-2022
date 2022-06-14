#!/usr/bin/env python

from dates import getToday, getYear

if int(getYear(getToday())) == 2020:
    print('It is still 2020!')
else:
    print('2020 is but a memory!')
