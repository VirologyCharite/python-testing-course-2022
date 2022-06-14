def unannotatedRegions(features, sequence):
    """
    Find unannotated regions and yield dictionaries with their info.

    @param features: An iterable of C{dict}s, each with a 'start' and
        'stop' key with an C{int} value.
    @param sequence: The C{str} DNA sequence containing the features.
    @return: A generator that yields C{dict}s with C{int} 'start' and
        'stop', and a C{str} 'sequence' subsequence.
    """
    annotatedOffsets = set()
    for feature in features:
        annotatedOffsets.update(range(feature["start"], feature["stop"]))

    start = None

    def makeNew(stop):
        return {
            "start": start,
            "stop": stop,
            "sequence": sequence[start:stop],
        }

    for offset in range(len(sequence)):
        if offset in annotatedOffsets:
            if start is not None:
                yield makeNew(offset)
                start = None
        else:
            if start is None:
                start = offset

    if start is not None:
        yield makeNew(offset + 1)
