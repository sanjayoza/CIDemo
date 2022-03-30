import unittest
import funcs

class TestCases(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def testAddIntegers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = funcs.add2(1, 2)
        self.assertEqual(result, 3)

    def testAddFloats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = funcs.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def testAddStrings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = funcs.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def testAddStringInteger(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = funcs.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def testAddStringNumber(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = funcs.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

if __name__ == '__main__':
    unittest.main()
