"""
202. Happy Number
Easy
9.7K
1.3K
Companies

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

 

Constraints:

    1 <= n <= 231 - 1


"""


class Solution:
    def isHappy(self,  n: int) -> bool:
        max_loop = 995
        def recur(val, max):
            max -= 1
            temp = 0
            for i in str(val):
                temp += int(i)**2
                print(temp, int(i)**2, i)
            if max == 0: return val 
            if int(str(temp)[::-1])  == 1 or temp == 1: return 1
            return recur(temp, max)
        rtrn = recur(n, max_loop)
        if rtrn == 1: return True
        else: return False
