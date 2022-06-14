from find_correct import unannotatedRegions


def testSimple():
    features = [
        {
            'start': 4,
            'stop': 7,
        },
    ]
    expected = [
        {
            'start': 0,
            'stop': 4,
            'sequence': 'ACGT',
        },
        {
            'start': 7,
            'stop': 8,
            'sequence': 'T',
        }
    ]
    result = list(unannotatedRegions(features, 'ACGTCCGT'))
    assert expected == result
