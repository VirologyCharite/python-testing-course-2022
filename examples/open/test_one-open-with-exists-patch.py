import os
import pytest
from unittest.mock import patch, mock_open
import builtins


def lineCounter(filename):
    if filename is None:
        raise ValueError(f'Non-existent file {filename!r}.')

    count = 0
    if os.path.exists(filename):

        if os.path.isdir(filename):
            raise ValueError(f'{filename} is a directory')

        with open(filename) as fp:
            for line in fp:
                count += 1

    return count


@patch('os.path.isdir')
def testOneOpenNoneFilename(isDirMock):
    isDirMock.return_value = False
    error = r'^Non-existent file None\.'
    with pytest.raises(ValueError, match=error):
        lineCounter(None)


@patch('os.path.isdir')
@patch('os.path.exists')
def testOneOpenSucceeds(existsMock, isDirMock):
    isDirMock.return_value = False
    data = '>id1\nACGT'
    with patch.object(builtins, 'open', mock_open(read_data=data)):
        assert lineCounter('non-existent-file.bam') == 2


@patch('os.path.isdir')
@patch('os.path.exists')
def testOneOpenFails(existsMock, isDirMock):
    existsMock.return_value = False
    data = '>id1\nACGT'
    with patch.object(builtins, 'open', mock_open(read_data=data)):
        assert lineCounter('non-existent-file.bam') == 0
