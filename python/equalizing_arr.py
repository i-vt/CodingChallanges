#https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        counter = 0
        while nums[0] != nums[-1]:
            # 7:10 start, 7:18 started timing
            rev_nums = nums[::-1]
            # took me 20 mins to trouble shoot the fact that I had to pull out the [::-1] to break it up into another variable
            for number in rev_nums:
                if nums[-1] > number: 
                    nums[-1] = number
                    counter += 1
                    break
            nums.sort()
        return counter
#Technically works, but apparently takes up too much memory :(

# Solution:
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                res += i

        return res
