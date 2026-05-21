class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = "zxyzxyx"
        """
        1. First we need to have a window l -> r from starting
        2. while r < len(n):
            if duplicate not found 
                add it to the map
            if found
                move the left pointer till the duplicate is removed and update the map till then

        """
        l = 0
        ans = 0
        map = set()

        for r in range(len(s)):
            while s[r] in map:
                map.remove(s[l])
                l += 1
            map.add(s[r])
            ans = max(ans, r-l+1)
        return ans
            

        