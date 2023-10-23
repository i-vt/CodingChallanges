"""
Food is being distributed, 1 person should get 1 plate, if their ranking is higher than their (direct) neighbors they should get more
Function is supposed to return a sum of food destributed - aiming to provide the least amount of food while maintaining the rules above

Dynamic programming, forward & backward pass, plus maximizing the sub-problem
"""

class Solution:
    def food(self, R):
        # Initialize variables: n is the length of input list R, and ans is a list of length n filled with 1s.
        n, ans = len(R), [1]*len(R)

        # First pass through the list
        for i in range(n-1):
            # Check if the satisfaction level at the current position is less than the next position.
            if R[i] < R[i+1]:
                # If yes, update the satisfaction level at the next position (ans[i+1]) to be the maximum of:
                # 1. The current satisfaction level plus 1 (1 + ans[i])
                # 2. The existing satisfaction level at the next position (ans[i+1])
                ans[i+1] = max(1 + ans[i], ans[i+1])

        # Second pass through the list (in reverse order)
        for i in range(n-2, -1, -1):
            # Check if the satisfaction level at the next position is less than the current position.
            if R[i+1] < R[i]:
                # If yes, update the satisfaction level at the current position (ans[i]) to be the maximum of:
                # 1. The satisfaction level at the next position plus 1 (1 + ans[i+1])
                # 2. The existing satisfaction level at the current position (ans[i])
                ans[i] = max(1 + ans[i+1], ans[i])

        # Return the sum of all satisfaction levels in the ans list.
        return sum(ans)

"""
# Results:
# 3 hours of cobbling stuff together got only 22/40 tests to pass lol.
# re-wrote the solution from scratch 4 times - yet still taking Ls 


class Solution:

    def food(self, ratings: List[int]) -> int:
        #12:07
        def chk(index):
            if len(ratings) > index and -1 < index: return True
            return False
        def mx(var1, var2):
            if var1 > var2: return var1
            return var2
        def mn(var1, var2):
            if var1 < var2: return var1
            return var2
        def chk_nei(index):
            if chk(index-1) and chk(index+1):
                if ratings[index-1] >= ratings[index] and ratings[index+1] >= ratings[index]:
                    return True
            return False
            
        sorted_ratings = ratings
        ratings.sort()
        set_ratings = set(ratings)
        counter = 1
        return_ratings = ratings
        for item in set_ratings:
            for k in range(len(ratings)):
                rating = ratings[k]
                if rating == item: return_ratings[k] = counter
            counter += 1
        for i in range(len(return_ratings)):
            if chk_nei(i) and len(return_ratings) != 3: return_ratings[i] = 1
        if len(ratings) > 2:
            if return_ratings[-2] >= return_ratings[-1]: return_ratings[-1] = 1
            if return_ratings[1] >= return_ratings[0]: return_ratings[0] = 1

        
        return sum(return_ratings)


            

"""
