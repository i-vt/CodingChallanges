"""
7. Reverse Integer
Medium
12.1K
13.1K
Companies

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1


"""


class Solution:
    def reverse(self, x: int) -> int:
        lst = (list(str(abs(x)))[::-1])
        new_int = ""
        for i in lst: new_int += str(i)
        new_int = int(new_int)
        if new_int > 2 ** 31 - 1 or new_int < -1 * 2**31: return 0
        if x >= 0: return new_int
        else: return new_int*-1
        
