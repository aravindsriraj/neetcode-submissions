class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n
        rightmax = -1

        for i in range(n-1,-1,-1):
            res[i] = rightmax
            rightmax = max(rightmax,arr[i])
        
        return res
        