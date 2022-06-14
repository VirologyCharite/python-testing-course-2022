import unittest
from random import uniform


def getExpensiveResource():
    value = uniform(1, 100)
    print(f'The expensive resource is {value!r}')
    return value


def releaseExpensiveResource(value):
    print(f'Releasing resource {value}')


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.expensive = getExpensiveResource()

    def tearDown(self):
        releaseExpensiveResource(self.expensive)

    def testOne(self):
        # Run pytest with pytest --capture=tee-sys to see this output.
        print(f'I will run some tests on resource {self.expensive!r}')
