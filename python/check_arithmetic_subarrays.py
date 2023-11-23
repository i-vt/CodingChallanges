class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        #12:35
        #12:44 had to ask chatGPT to clarify the probem statement
        arr_return = []
        for counter in range(len(l)):
            new_arr = nums[l[counter]:r[counter]+1]
            new_arr.sort()
            
            if new_arr[0] == new_arr[::-1]: arr_return.append(True)
            else:
                diff = []
                for i in range(1, len(new_arr)):
                    diff.append(new_arr[i-1] - new_arr[i])
                
                if len(set(diff)) > 1: arr_return.append(False)
                else: arr_return.append(True)

                """len_nums =len(new_arr)
                #sub_arr1 = new_arr[0]
                
                if len_nums % 2 == 1: 
                    middle = math.floor(len_nums/2)
                    median =  new_arr[middle]
                    if abs(middle - sum(new_arr[:middle])) != abs(middle - sum(new_arr[middle:])): 
                        arr_return.append(False)
                        continue

                else:
                    half_len_nums = math.ceil(len_nums / 2)
                    middle = half_len_nums
                    median=  ( new_arr[half_len_nums] + new_arr[half_len_nums-1] ) /2
                
                    if abs(middle - sum(new_arr[:middle-1])) != abs(middle - sum(new_arr[middle:])): 
                        arr_return.append(False)
                        continue
                arr_return.append(True)"""
        
        return arr_return
# break 1:00; resume 1:13 - 1:14; 1:38-1:50
# 25 + 1 + 12 = 38 mins
