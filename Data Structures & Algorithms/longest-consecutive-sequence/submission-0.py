class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for num in s:
            # only start counting from the beginning of a sequence
            if num - 1 not in s:
                length = 1
                curr = num

                while curr + 1 in s:
                    curr += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len