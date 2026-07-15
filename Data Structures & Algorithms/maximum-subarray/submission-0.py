class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(curr_sum,0)
            curr_sum+=n
            maxSum = max(maxSum,curr_sum)
        return maxSum
        