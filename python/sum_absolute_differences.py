class Solution:
    def getSumAbsoluteDifferences(nums: list[int]) -> list[int]:
        #15 mins to resolve, couldn't figure out how to optmize, but created multiple differnt ways
        leng = len(nums)
        summ = sum(nums)
        maxi = max(nums)
        mini = min(nums)
        sortf = nums
        sortf.sort()
        sortr = sortf[::-1]
        rtn = []
        for num in nums:
            sub1 = 0
            for num1 in nums:
                sub1 += abs(num - num1)


            var1 = num*leng
            if summ < var1: 
                sub = int(abs(var1 - summ))
            else:
                sub = int(abs(summ-var1))

            #rtn.append(sub)

            index1 = sortf.index(num)

            index2 = leng - sortr.index(num)

            sub2 = (num*len(nums[:index1]) - sum(nums[:index1])) +  sum(nums[index2:]) - num*len(nums[index2:]) 

            print(sub,sub1, sub2, nums[:index1], nums[index2:])


            rtn.append(sub)
        return rtn


"""

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sm,pr=sum(nums),0
        for i in range(len(nums)):
            pr+=nums[i]
            nums[i]=(((i+1)*nums[i]-pr)+(sm-pr)-(len(nums)-i-1)*nums[i])
        return nums

"""
