import sys
from io import StringIO


def lineCounter(fp):
    count = 0
    for line in fp:
        count += 1

    return count


def testOneOpen():
    print("We are in the test!", file=sys.stderr)
    assert lineCounter(StringIO('>id1\nACGT')) == 2
