#!/usr/bin/env python

import sys
from dates import getToday, getYear

try:
    today = sys.argv[1]
except IndexError:
    today = getToday()

print('The year is', getYear(today))
