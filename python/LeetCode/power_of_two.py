"""
231. Power of Two
Easy
6.1K
386
Companies

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 

Constraints:

    -231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""




class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if "0" not in str(bin(n)).split("b")[1]: return True
        #if n < 1 or n > 2**30: return False
        
        twopower = """1
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
32768
65536
131072
262144
524288
1048576
2097152
4194304
8388608
16777216
33554432
67108864
134217728
268435456
536870912
1073741824""".split("\n")
        return str(n) in twopower
        from math import log
        print(log(n, 2) % 1)
        if log(n, 2) % 1 > 0: return False
        # For some mf reason log of 2^29 base 2 kept returning a non 0 :(((
        return True

        #536870912
        
