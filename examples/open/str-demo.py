#!/usr/bin/env python

import sys
from io import StringIO

oldStdout = sys.stdout
newStdout = StringIO()

sys.stdout = newStdout

print('hello')

sys.stdout = oldStdout

print(f'PRINTED: {newStdout.getvalue()}')
