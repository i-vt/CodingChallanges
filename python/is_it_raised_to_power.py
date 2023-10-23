"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

Constraints:

    -2**31 <= n <= 2**31 - 1
 Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n <= 0: return False #at no point 4^x should be 0 or below - because even when 4^-10 = 9.53 * 10^-7 or 4^0 = 1; it can get very close to 0, but never 0 (unless it gets rounded to it lol)
        if math.log(n,4) % 1 > 0: return False
        return True
# I remembered cool think called log - so it took me only 6 minutes with 2 re-runs b/c of 1 typo & 1 forgot to handle n<=0 lol
# Nit-picks: probably could memorize the syntax for math.log(n,4) - instead of googling it lol
