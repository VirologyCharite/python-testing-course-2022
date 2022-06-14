#!/usr/bin/env python

import sys
from dates import getToday, getDay

try:
    today = sys.argv[1]
except IndexError:
    today = getToday()

print('The day is', getDay(today))
