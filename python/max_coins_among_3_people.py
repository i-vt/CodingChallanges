"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/?envType=daily-question&envId=2023-11-24

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

    In each step, you will choose any 3 piles of coins (not necessarily consecutive).
    Of your choice, Alice will pick the pile with the maximum number of coins.
    You will pick the next pile with the maximum number of coins.
    Your friend Bob will pick the last pile.
    Repeat until there are no more piles of coins.

Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
"""


class Solution:
    
  
  
  def maxCoins(self, piles: List[int]) -> int:
        
        #4:43 20 to solve, 20 to optimize (many reruns)
        piles.sort()
        counter = 0
        leng = len(piles)
        triplets = int(leng/3) # For some reason this returned floats like 3.0000 instead of 3 :( 
        piles = piles[triplets:]
        for _ in range(triplets):
            counter += piles[-2]
            piles = piles[:-2]

        """while len(piles) != 0:
            counter += piles[-2]
            piles = piles[1:-2]
        """
        return counter 


"""
Acceptetd solutions (more optimized than mine)

class Solution:
    def maxCoins(self, piles):
        piles.sort()
        total_coins = 0
        pair = len(piles) // 3
        for i in range(pair, len(piles), 2):
            total_coins += piles[i]
        return total_coins




class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])
"""
