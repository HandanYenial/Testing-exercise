from unittest import TestCase
from examples import reverse_str,is_palindrome,factorial

class ExamplesTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('learn'), 'nrael')
        self.assertEqual(reverse_str('Banana'), 'ananaB')
        #wanted to check if the casing is maintained.
        
    def test_is_palindrome(self): #it is a boolean function, so we will check if it is true or false
        self.assertTrue(is_palindrome('racecar'))
        #self.assertTrue(is_palindrome('learn')) #will give an error since it is not true
        self.assertFalse(is_palindrome('learn'))
        self.assertTrue(is_palindrome('RaceCar')) #it will ignore the capital letter since in the function, .lower
        
    def test_factorial(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(3),6)
        #as written in our function, it will raise a value error when there is a negative number
        #then if there is a negative number, it will stop running our function due to the error
        #to deal with that we can use assertRaises:checking if there is an exception is raised
        #assertRaises(exception we are waiting to have,pass the function, arguments that we will pass in the function)
        self.assertRaises(ValueError, factorial, -9)
        # I want to try what will happen if I pass a float
        self.assertRaises(ValueError, factorial, 4.8)
        
        
        #Method	           Checks that
#assertEqual(a, b)	         a == b
#assertNotEqual(a, b)	     a != b
#assertTrue(x)          	 bool(x) is True
#assertFalse(x)	            bool(x) is False
#assertIs(a, b)	            a is b
#assertIsNot(a, b)       	a is not b
#assertIsNone(x)	        x is None
#assertIsNotNone(x)	        x is not None
#assertIn(a, b)     	    a in b
#assertNotIn(a, b)  	    a not in b
#assertIsInstance(a, b)   	isinstance(a, b)
#assertNotIsInstance(a, b) 	not isinstance(a, b)
