from find_ORF import findORF


class TestFindORF:
    """
    Tests for the findORF method.
    """
    def testEmpty(self):
        """
        If an empty read is passed we must get back a dictionary indicating
        failure to find anything.
        """
        assert findORF("", 0) == {
            "foundStartCodon": False,
            "foundStopCodon": False,
            "length": 0,
            "translation": "",
        }

    def testLengthOne(self):
        """
        If a read of length one is passed we must get back a dictionary
        indicating failure to find anything.
        """
        assert findORF("A", 0) == {
            "foundStartCodon": False,
            "foundStopCodon": False,
            "length": 0,
            "translation": "",
        }

    def testLengthTwo(self):
        """
        If a read of length two is passed we must get back a dictionary
        indicating failure to find anything.
        """
        assert findORF("AT", 0) == {
            "foundStartCodon": False,
            "foundStopCodon": False,
            "length": 0,
            "translation": "",
        }

    def testOffsetOutOfRange(self):
        """
        If an out-of-range offset is passed we must get
        back a dictionary indicating failure to find anything.
        """
        assert findORF("", 10) == {
            "foundStartCodon": False,
            "foundStopCodon": False,
            "length": 0,
            "translation": "",
        }

    def testRequireStartCodon(self):
        """
        If a start codon is required but is not present we must get back a
        dictionary indicating failure to find anything.
        """
        assert findORF("CCAGG", 0, requireStartCodon=True) == {
            "foundStartCodon": False,
            "foundStopCodon": False,
            "length": 0,
            "translation": "",
        }

    def testOnlyStartCodon(self):
        """
        If a read consists just of a start codon must get the expected
        result.
        """
        assert findORF("ATG", 0) == {
            "foundStartCodon": True,
            "foundStopCodon": False,
            "length": 1,
            "translation": "M",
        }

    def testOnlyStartStopCodon(self):
        """
        If a read consists just of a start codon and then a stop codon,
        we must get the expected result.
        """
        assert findORF("ATGTAG", 0) == {
            "foundStartCodon": True,
            "foundStopCodon": True,
            "length": 2,
            "translation": "M*",
        }

    def testStartAndNoStopCodon(self):
        """
        If a read consists just of a start codon and then a non-stop codon,
        we must get the expected result.
        """
        assert findORF("ATGTCC", 0) == {
            "foundStartCodon": True,
            "foundStopCodon": False,
            "length": 2,
            "translation": "MS",
        }

    def testNonZeroOffset(self):
        """
        If the start codon is at a non-zero offset we must get the
        expected result.
        """
        assert findORF("GATGTCC", 1) == {
            "foundStartCodon": True,
            "foundStopCodon": False,
            "length": 2,
            "translation": "MS",
        }
