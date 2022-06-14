from unittest.mock import patch, mock_open
import builtins


def lineCounter(filename):
    count = 0
    with open(filename) as fp:
        for line in fp:
            count += 1

    return count


def testOneOpen():
    data = '>id1\nACGT\nhey\nyou\n'
    with patch.object(builtins, 'open', mock_open(read_data=data)):
        assert lineCounter('non-existent-file.bam') == 4
