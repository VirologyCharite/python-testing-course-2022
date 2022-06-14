from unittest import TestCase


class TestFailure(TestCase):

    def testX(self):
        """
        Test that p is 10.
        """
        p = 10
        self.assertTrue(p, 10)
