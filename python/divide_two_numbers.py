"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = "AaaaaAAaaAaaAAaa"
        if abs(dividend) < abs(divisor): return 0
        if dividend == divisor: return 1
        int_big, int_small = abs(dividend), abs(divisor)
        counter = 0
        
        while int_big >= int_small and int_small != 1:
            int_big -= int_small
            counter += 1
        if int_small == 1: 
            counter = abs(dividend)
        if dividend > 0 and divisor > 0: return counter
        if dividend > 0 or divisor > 0: return -abs(counter)
        return counter
