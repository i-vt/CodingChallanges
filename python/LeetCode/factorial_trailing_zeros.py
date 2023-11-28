"""
172. Factorial Trailing Zeroes
Medium
3K
1.9K
Companies

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0

 

Constraints:

    0 <= n <= 104

 

Follow up: Could you write a solution that works in logarithmic time complexity?

"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n in [0,1,2]: return 0
        lst = list(range(3,n+1))
        counter = 2
        for i in lst:
            counter = counter * i
        import sys
        sys.set_int_max_str_digits(0)
        max = len(str(counter)) 
        rev = int(str(counter)[::-1])
        return max - len(str(rev))



        
