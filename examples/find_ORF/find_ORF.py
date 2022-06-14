from Bio.Seq import translate

START_CODON = 'ATG'
STOP_CODONS = set('TAA TAG TGA'.split())


def findORF(sequence, offset, requireStartCodon=True):
    """
    Find an ORF that supposedly starts at a specified offset in a DNA
    sequence.

    @param offset: The C{int} offset of the start codon.
    @param requireStartCodon: If C{True}, the first codon must be a start
        codon. If it is not, the search is abandoned immediately and the
        returned dictionary will have zero, C{False}, and empty values.
    @return: A C{dict} with C{str} keys:
        length (int): the length of the ORF (in amino acids).
        foundStartCodon (bool): if a start codon was found.
        foundStopCodon (bool): if a stop codon was found.
    """
    first = True
    length = 0
    foundStartCodon = foundStopCodon = False
    codons = []

    for index in range(offset, len(sequence), 3):
        codon = sequence[index:index + 3]
        if len(codon) != 3:
            break

        if first:
            first = False
            if codon == START_CODON:
                foundStartCodon = True
            elif requireStartCodon:
                break

        length += 1
        codons.append(codon)

        if codon in STOP_CODONS:
            foundStopCodon = True
            break

    return {
        'length': length,
        'foundStartCodon': foundStartCodon,
        'foundStopCodon': foundStopCodon,
        'translation': translate(''.join(codons)),
    }
