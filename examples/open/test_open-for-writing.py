from unittest.mock import patch
from io import StringIO
import builtins


# Test with an open file pointer.


def lineWriterFp(fp):
    print('we are here', file=fp)


def test_lineWriterFp():
    output = StringIO()
    lineWriterFp(output)
    assert output.getvalue() == 'we are here\n'


# Test with a filename.


def lineWriterFilename(filename):
    with open(filename, 'w') as fp:
        print(f'The fp is {fp!r}.')
        print('we are here too', file=fp)


def test_lineWriterFilename():

    class Open:
        def __init__(self, output):
            self.output = output

        def sideEffect(self, filename, *args, **kwargs):

            if 'w' in args:
                return self.output

            else:
                raise RuntimeError(
                    f'Not called to write a file! Filename: {filename!r}, Args: '
                    f'{args!r}, Keyword args: {kwargs!r}.')

    output = StringIO()
    output.close = lambda: 33

    sideEffect = Open(output).sideEffect

    with patch.object(builtins, 'open') as mockMethod:
        mockMethod.side_effect = sideEffect

        lineWriterFilename('xxx')

        assert output.getvalue() == 'we are here too\n'
