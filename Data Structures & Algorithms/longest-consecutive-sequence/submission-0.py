class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            # check if n is the start of the sequence
            if n-1 not in hashset:
                length = 0
                while (n + length) in hashset:
                    length += 1
                longest = max(longest, length)
        return longest