class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums)-1: return True

        if nums[0] == 0: return False

        if nums[-1] == 0: nums = nums[:-1]

        """
        split = nums.split(0)
        for i in split:
            if [] == i: continue
            if max(i) < len(i) + 1 or i[-1] >= 2: continue
            return False
        """
        zeros = nums.count(0)

        for i in range(zeros):
            index = nums.index(0)
            Good = False
            for i in range(index):
                if i + nums[i] > index:
                    Good = True
                    break
            if Good == False: return Good
            nums[index] = -1
        
        # 38 mins to complete with 3 errors (1 typo, 2 logic issues)
        # Should aim at lower than 30 mins, preferably with 1 or lower reruns.
        # Forgot to rename "Good" variable & slap comments on top of it

        return True
                
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the farthest reachable index
        farthest_reachable = 0

        # Iterate through the array
        for i, jump_length in enumerate(nums):
            # Check if the current index is beyond the farthest reachable point
            if i > farthest_reachable:
                return False

            # Update the farthest reachable index
            farthest_reachable = max(farthest_reachable, i + jump_length)

            # Early exit if the end of the array is already reachable
            if farthest_reachable >= len(nums) - 1:
                return True

        # Return whether the last index is reachable
        return farthest_reachable >= len(nums) - 1

# Uses greedy approach
"""
