# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(nums: list, k: int) -> int:

        
        def diff(arr_passed: list, int_passed: int) -> list:
            arr_return = []
            for item in arr_passed:
                if item >= int_passed:
                    arr_return.append(int_passed-item)
                
            return arr_return
        
        def combo(arr_passed: list, int_passed: int) -> int:
            arr_passed.sort()
            arr_passed = arr_passed[::-1]
            counter = 0
            for item in arr_passed:
                if int_passed <= 0 or item + int_passed < 0 : return counter
                
                int_passed += item
                counter += 1
            return counter

        final_counter = 0
        for number in nums:
            
            subset = diff(nums, number)
            #print(subset)
            max_temp = combo(subset, k)
            #print(max_temp)
            if max_temp > final_counter: final_counter = max_temp
        return final_counter


# Not optimized but works. Took around 45 minutes to get it to functional state with multiple reruns. LC did not accept my solution lol - bc apparently it ran out of resources
