import math
class Solution:
    def calc(self, piles, mid, h):
        res = 0
        for num in piles:
            res+=math.ceil(num/mid)
        return res
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low<=high:
            mid = (low+high)//2
            res = self.calc(piles,mid,h)
            if res<=h:
                high = mid-1
            else:
                low = mid+1
        return low

        