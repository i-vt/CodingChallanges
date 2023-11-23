"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

class Solution:
    import math
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
      #Solve-time 15 to 20 minutes

        # 5th rerun successful.
        # 2 logic errors & 2 typos

        nums = nums1+nums2

        nums.sort()
        len_nums = len(nums)
        if len_nums % 2 == 1: 
            return nums[math.floor(len_nums/2)]
        else:
            half_len_nums = math.ceil(len_nums / 2)
            return ( nums[half_len_nums] + nums[half_len_nums-1] ) /2
            # 1 2; 1, 2 , 3 , 4 
