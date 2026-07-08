class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for num in nums:
            if num==1:
                c+=1
                res = max(res,c)
            else:
                c = 0
        return res

        