import pytest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import builtins


def lineCounter(filename):
    count = 0
    with open(filename, 'r') as fp:
        for line in fp:
            count += 1

    return count


class Test(TestCase):
    """
    Do it with unittest, subclassing TestCase.
    """

    def testTwoCallsToOpen(self):

        class Open:
            def __init__(self, test):
                self.test = test
                self.count = 0

            def sideEffect(self, filename, *args, **kwargs):
                if self.count == 0:
                    self.test.assertEqual('filename1.fasta', filename)
                    self.count += 1
                    return StringIO('>id1\nACTG\n>id2\nAACCTTGG\n')
                elif self.count == 1:
                    self.test.assertEqual('filename2.fasta', filename)
                    self.count += 1
                    return StringIO('>id2\nAAACCC\n')
                else:
                    raise RuntimeError(
                        f'Open called too many times. Filename: {filename!r},'
                        f'Args: {args!r}, Keyword args: {kwargs!r}.')

        with patch.object(builtins, 'open') as mockMethod:
            mockMethod.side_effect = Open(self).sideEffect

            self.assertEqual(4, lineCounter('filename1.fasta'))
            self.assertEqual(2, lineCounter('filename2.fasta'))

            error = 'too many times'
            self.assertRaisesRegex(RuntimeError, error, lineCounter, 'filename3.fasta')


# Do it with pytest.

def test_TwoCallsToOpen():

    class Open:
        def __init__(self):
            self.count = 0

        def sideEffect(self, filename, *args, **kwargs):
            if self.count == 0:
                assert filename == 'filename1.fasta'
                self.count += 1
                return StringIO('>id1\nACTG\n>id2\nAACCTTGG\n')
            elif self.count == 1:
                assert filename == 'filename2.fasta'
                self.count += 1
                return StringIO('>id2\nAAACCC\n')
            else:
                raise RuntimeError(
                    f'Open called too many times. Filename: {filename!r}, Args: '
                    f'{args!r}, Keyword args: {kwargs!r}.')

    sideEffect = Open().sideEffect
    with patch.object(builtins, 'open') as mockMethod:
        mockMethod.side_effect = sideEffect

        assert lineCounter('filename1.fasta') == 4
        assert lineCounter('filename2.fasta') == 2

        error = 'too many times'
        with pytest.raises(RuntimeError, match=error):
            lineCounter('filename3.fasta')
