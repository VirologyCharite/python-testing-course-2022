import pytest

from find import unannotatedRegions


def testSimple():
    features = [
        {
            'start': 4,
            'stop': 7,
        },
    ]
    result = list(unannotatedRegions(features, 'ACGTCCGT'))
    expected = [
        {
            'start': 0,
            'stop': 4,
            'sequence': 'ACGT',
        }
    ]
    assert expected == result


def testNoFeatures():
    features = []
    result = list(unannotatedRegions(features, 'ACGTCCGT'))
    expected = [
        {
            'start': 0,
            'stop': 8,
            'sequence': 'ACGTCCGT',
        }
    ]
    assert expected == result


@pytest.mark.xfail(reason='No return of the final unannotated region.')
def testSimple2():
    features = [
        {
            'start': 4,
            'stop': 7,
        },
    ]
    result = list(unannotatedRegions(features, 'ACGTCCGTAA'))
    expected = [
        {
            'start': 0,
            'stop': 4,
            'sequence': 'ACGT',
        },
        {
            'start': 8,
            'stop': 10,
            'sequence': 'AA',
        }
    ]
    assert expected == result
