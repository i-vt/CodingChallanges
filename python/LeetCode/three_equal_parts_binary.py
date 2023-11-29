"""
927. Three Equal Parts
Hard
815
119
Companies

You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

    arr[0], arr[1], ..., arr[i] is the first part,
    arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
    arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
    All three parts have equal binary values.

If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]

Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]

Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]

"""


# Fucked up the optimization lol - couln't solve past 100 due to timeout issues
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def inttobin(binary):
            rtrn = ""
            for i in binary: rtrn += str(i)
            return int(str(rtrn),2)
        
        """
        temp = []
        firstval = False
        for i in arr: 
            if i == 0 and firstval == False and len(set(arr)) > 1: continue
            else:
                firstval = True
                temp.append(i)
        count = len(arr) - len(temp)
        """


        """
        if len(arr) > 100:
            first = True
            temp = ""
            for i in arr: 
                if str(i) == "0" and first: continue
                temp += str(i)
                temp
        """
        
        ### Failed optimization
        ones = [i for i, j in enumerate(arr) if j==1]

        if len(ones) % 3 > 0: return [-1,-1]
        


        start, end = 1, len(arr)


        if len(arr) > 100: start = int(len(arr)/4)
        ####

        for i1 in range(start, len(arr)-1):
            #if i1 < count: continue
            for i2 in range(i1, len(arr)):
                if i1 >= i2: continue
                int1 = inttobin(arr[:i1])
                int2 = inttobin(arr[i1:i2])
                int3 = inttobin(arr[i2:])
                if int1 == int2 and int2 == int3: return [i1-1,i2]
        return [-1,-1]









"""
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
        ones = [i for i, j in enumerate(arr) if j==1]
        n=len(ones)

        if not ones:
            return [0, 2]
        if n%3:
            return [-1, -1]
        
        i,j,k = ones[0], ones[n//3], ones[n//3*2]
        l = len(arr)-k

        if arr[i:i+l]==arr[j:j+l]==arr[k:k+l]:
            return [i+l-1, j+l]

        return [-1, -1]
"""


"""
    enumerate(arr): This function is used to iterate over the elements of the arr list while keeping track of their indices. It returns pairs of (index, value) for each element in arr.

    for i, j in enumerate(arr): This part of the code iterates over each element in arr, and for each element, it assigns the index to i and the value to j.

    if j == 1: This is a conditional statement that checks if the value j is equal to 1. If the condition is true, the corresponding index i is included in the list comprehension.

    [i for i, j in enumerate(arr) if j == 1]: This is a list comprehension that creates a list of indices (i) for elements in arr where the value (j) is equal to 1. So, the ones list will contain the indices of all occurrences of 1 in the arr list.
"""

        
