class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        mx = float("-inf")
        while i<j:
            area = (j-i) * min(heights[i],heights[j])
            mx = max(area,mx)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return mx
        