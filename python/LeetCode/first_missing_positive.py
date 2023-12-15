class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        """
        if nums[0] > 1 or nums[-1] < 1: return 1
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if nums[i]+1 > 0: return nums[i]+1
                else: return 1
        
        return nums[-1]+1
        """

        """
        if len(nums)> 150: 
            max = 30
            for i in range(1,max +1):
                if i not in nums: return i
            for i in range(len(nums), len(nums)-30, -1):
                if i not in nums: return i
        else:
             for i in range(1,len(nums)+1):
                if i not in nums: return i           
        return nums[-1] + 1
        """
        nums.sort()
        if 1 not in nums: return 1
        var1 = list(set(list(range(1, len(nums)+1))) - set(nums))
        if var1 != []: return min(var1)
        else: return nums[-1] +1
        
