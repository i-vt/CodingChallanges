class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        counter = 0
        while nums[0] != nums[-1]:
            # 7:10 start, 7:18 started timing
            rev_nums = nums[::-1]
            for number in rev_nums:
                if nums[-1] > number: 
                    nums[-1] = number
                    counter += 1
                    break
            nums.sort()
        return counter
