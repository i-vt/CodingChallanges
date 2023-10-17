

"""
Smallest K numbers of an array:
unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
smallest = smallest_k(unsorted, 5)
print(smallest)
[-2, 0, 1, 1, 4]
"""

import unittest, logging

logging.basicConfig(level=logging.DEBUG)  
objLogger = logging.getLogger(__name__)

"""
Level; Numeric value; What it means / When to use it
logging.NOTSET; 0; When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to NOTSET, then all events are logged. When set on a handler, all events are handled.
logging.DEBUG; 10; Detailed information, typically only of interest to a developer trying to diagnose a problem.
logging.INFO; 20; Confirmation that things are working as expected.
logging.WARNING; 30; An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected.
logging.ERROR; 40; Due to a more serious problem, the software has not been able to perform some function.
logging.CRITICAL; 50; A serious error, indicating that the program itself may be unable to continue running.
"""

# Sample
def quickSort_Pythonic(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quickSort_Pythonic(left) + [pivot] + quickSort_Pythonic(right)
 
def quickSort(arrPassed: list = [], bolDebugging: bool = False) -> list:
	if len(arrPassed) <= 1: return arrPassed
	intPivot = arrPassed[0]
	arrLeft, arrRight = [], []
	for intItem in arrPassed[1:]:
		if intItem < intPivot: arrLeft.append(intItem)
	for intItem in arrPassed[1:]:
		if intItem >= intPivot: arrRight.append(intItem)
	if bolDebugging: 
		objLogger.error(f"arrLeft = {arrLeft} | intPivot = {intPivot} | arrRight = {arrRight}")
	return quickSort(arrLeft) + [intPivot] + quickSort(arrRight)

"""
[1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
arrLeft = [-2, 0] | intPivot = 1 | arrRight = [7, 4, 1, 10, 9, 10, 10]
arrLeft = [] | intPivot = -2 | arrRight = [0]
arrLeft = [4, 1] | intPivot = 7 | arrRight = [10, 9, 10, 10]
arrLeft = [1] | intPivot = 4 | arrRight = []
arrLeft = [9] | intPivot = 10 | arrRight = [10, 10]
arrLeft = [] | intPivot = 10 | arrRight = [10]
[-2, 0, 1, 1, 4, 7, 9, 10, 10, 10]
"""

def getSmallestFromArr(arrPassed: list = [], intQuantity: int = 1, bolDebugging: bool = False) -> list:
	for intValue in arrPassed:
		if type(intValue) != type(1):
			if bolDebugging: objLogger.error(f"ERROR: Removing invalid value: {intValue} from {arrPassed}")
			arrPassed.remove(intValue)
	if type(intQuantity) != type(1): 
		if bolDebugging: objLogger.error(f"ERROR: intQuantity invalid: {intQuantity}; replacing it with 1")
		intQuantity = 1
	if arrPassed == []: return []
	if intQuantity < 1 or intQuantity > len(arrPassed): intQuantity = 1

	arrReturn = quickSort(arrPassed)
	return arrReturn[:int(intQuantity)]


class test_getSmallestFromArr(unittest.TestCase):
	arrKnownGood_Unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
	arrKnownGood_Sorted = [-2, 0, 1, 1, 4, 7, 9, 10, 10, 10]
	arrKnownBad_Blank = []
	arrKnownBad_Alphanumeric = [1, 8, 3, "a", 109, 40]
	arrKnownGood_AlphanumericSorted = [1, 3, 8, 40, 109]




	def test_quickSort(self):
		self.assertEqual(quickSort(self.arrKnownGood_Unsorted), self.arrKnownGood_Sorted)
		self.assertEqual(quickSort_Pythonic(self.arrKnownGood_Unsorted), self.arrKnownGood_Sorted)
	def test_getSmallestFromArr(self):
		arrKnownBad_intQuantity = [-1, 0, 99999]
		arrKnownBad_strQuantity = ["-1", "1", "a"]
		arrKnownGood_intQuantity = [1, 2, 3 ,4, len(self.arrKnownGood_Sorted)]
		arrKnwonGood_Results = [[-2], [-2, 0], [-2, 0, 1], [-2, 0, 1, 1], self.arrKnownGood_Sorted]
		for intItem in arrKnownBad_intQuantity:
			self.assertEqual(getSmallestFromArr(self.arrKnownGood_Unsorted, intItem), [self.arrKnownGood_Sorted[0]])
		for strItem in arrKnownBad_strQuantity:
			self.assertEqual(getSmallestFromArr(self.arrKnownGood_Unsorted, strItem), [self.arrKnownGood_Sorted[0]])
		for intItem in range(len(arrKnownGood_intQuantity)-1):
			self.assertEqual(getSmallestFromArr(self.arrKnownGood_Unsorted, arrKnownGood_intQuantity[intItem]), arrKnwonGood_Results[intItem])





if __name__ == '__main__':
	unittest.main()











"""
Code review notes:
* Spent too long on the code + too many retries, should be striving for Senior results
  Junior (about 1 hour) with 5+ re-runs
  Mid-level (less than 30 mins) with up to 3 re-runs
  Senior (at most 15 mins) with up to 2 re-runs

* Lack of code comments:
  Example of production-grade comment
	def get_smallest_elements(input_list: list = [], int_quantity: int = 1, debug_mode: bool = False) -> list:
	    '''
	    Get the smallest elements from a list.

	    Args:
	        input_list (list): The input list to extract elements from.
	        int_quantity (int): The number of smallest elements to retrieve.
	        debug_mode (bool): Enable debugging mode.

	    Returns:
	        list: A list containing the smallest elements.
		'''
* Unnecessary unittests
  Imo if taking time to write out unittests unnecessary in this case, as it is a simple coding challange. If tested IRL, just talk through the implemented safe-guards and edge-case handling.
  The unittests are not needed for most of the interview questions, unless you going for a role that involves a strong emphasis on test-driven development (TDD) or the development of production-quality code.

* Funky unit tests
  Write just enough tests to cover the most critical functionality.
  Prioritize correctness over test coverage.

  Split up the tests critical functionality (not all in 1 class):
	class TestQuickSort(unittest.TestCase):
	    def setUp(self):
	        self.arrKnownGood_Unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
	        self.arrKnownGood_Sorted = [-2, 0, 1, 1, 4, 7, 9, 10, 10, 10]

	    def test_quickSort(self):
	        result = quickSort(self.arrKnownGood_Unsorted)
	        self.assertEqual(result, self.arrKnownGood_Sorted)

	    def test_quickSort_Pythonic(self):
	        result = quickSort_Pythonic(self.arrKnownGood_Unsorted)
	        self.assertEqual(result, self.arrKnownGood_Sorted)

	class TestGetSmallestFromArr(unittest.TestCase):
	    def setUp(self):
	        self.arrKnownGood_Unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
	        self.arrKnownGood_Sorted = [-2, 0, 1, 1, 4, 7, 9, 10, 10, 10]

	    def test_getSmallestFromArr_InvalidInputs(self):
	        invalid_inputs = [-1, 0, 99999, "-1", "1", "a"]
	        for input_value in invalid_inputs:
	            with self.subTest(input=input_value):
	                result = getSmallestFromArr(self.arrKnownGood_Unsorted, input_value)
	                self.assertEqual(result, [self.arrKnownGood_Sorted[0]])

	    def test_getSmallestFromArr_ValidInputs(self):
	        valid_inputs = [1, 2, 3, 4, len(self.arrKnownGood_Sorted)]
	        expected_results = [[-2], [-2, 0], [-2, 0, 1], [-2, 0, 1, 1], self.arrKnownGood_Sorted]
	        for input_value, expected_result in zip(valid_inputs, expected_results):
	            with self.subTest(input=input_value):
	                result = getSmallestFromArr(self.arrKnownGood_Unsorted, input_value)
	                self.assertEqual(result, expected_result)



* Remove unused (dead) code:
  If you want keep it in your notes, but not in a prod env. 
  arrKnownBad_Blank = []

FORMATTING:
* Fked up naming convention for variables:
   "Hungarian notation (strVariable or getSmallestFromArr) is generally considered inappropriate and non-idiomatic in Python, it is more common in statically-typed languages like C or C++,"
   Python's naming conventions (PEP 8) recommend using lowercase letters and underscores for variable and function names (i.e., snake_case), making variable names more human-readable.

* Constants variables probably should be in caps 
  arrKnownGood_Unsorted -> TEST_INPUT_UNSORTED_VALID (even that is a bit verbose tho)


NITPICKS:
* Might wanna use constants instead of retyping type(1)

* Do not use print for debugging stuff - use logging 
	import logging
	logging.basicConfig(level=logging.DEBUG)  
	logger = logging.getLogger(__name__)
	logger.error("Somen brok :)")

* Preferably don't sling class-level variables without setup - otherwise they can get lost in code
	class TestQuickSort(unittest.TestCase):
	    def setUp(self):
	        self.arrKnownGood_Unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
	        self.arrKnownGood_Sorted = [-2, 0, 1, 1, 4, 7, 9, 10, 10, 10]

* Use vim or neovim
  Stop using tabs, use spaces - you can configure vim to replace tabs with spacing
  make sure you learn majority of pre-defined short-cuts so your hands stay on the sauce at all times. + don't forget to customize ur own configs

* Hands on the keyboard, avoid keying back&forth for opening & closing {[""]}

* Might be a good idea to document thought-process via comments at least in the beginnnig (remove after done)

* Keep in mind fastest/shortest python solution is
	def smallest_k(arr, k):
	    arr.sort()
	    result = arr[:k]
	    return result
	unsorted = [1, 7, 4, 1, 10, 9, -2, 10, 10, 0]
	smallest = smallest_k(unsorted, 5)
	print(smallest)
"""




