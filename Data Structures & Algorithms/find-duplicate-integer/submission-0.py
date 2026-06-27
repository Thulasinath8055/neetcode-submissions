class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = set()
        for num in nums:
            if num not in map:
                map.add(num)
            else:
                return num
        