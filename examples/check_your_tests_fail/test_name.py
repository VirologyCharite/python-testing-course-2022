from unittest import TestCase


class PCR:
    def __init__(self, id_, result, date, testCentre, testCentreCategory=None):
        self.id_ = id_
        self.result = result
        self.date = date
        self.testCentre = testCentre
        if testCentreCategory is None:
            if 'sports medicine' in testCentre.lower():
                self.testCentreCategory = 'SM'
            else:
                self.testCentreCategory = 'Unknown'
        else:
            self.testCentreCategory = testCentreCategory


class TestPCR(TestCase):
    """
    Test the PCR class.
    """
    def testCentreCategoryAttribute(self):
        """
        Here is a test that works fine.
        """
        pcr = PCR('id', 'neg', '12/3/2020', 'A test centre', 'WD')
        self.assertEqual('WD', pcr.testCentreCategory)

    def testCentreCategoryNotPassed(self):
        """
        If no test centre category is passed, it must be correctly determined
        in __init__ from the full test centre name.
        """
        pcr = PCR('id', 'neg', '12/3/2020', 'A sports medicine test centre')
        self.assertEqual('SM', pcr.testCentreCategory)

    def centreCategoryNotPassed_THIS_SHOULD_FAIL_BUT_DOES_NOT(self):
        """
        If no test centre category is passed, it must be correctly determined
        in __init__ from the full test centre name.
        """
        pcr = PCR('id', 'neg', '12/3/2020', 'Another sports medicine centre')
        self.assertEqual('XP', pcr.testCentreCategory)
