class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        freq = {}
        res = 0

        for r in range(len(s)):
            #include new char
            freq[s[r]] = freq.get(s[r], 0) + 1


            max_freq = max(max_freq, freq[s[r]])
            windowsize = r-l+1

            #invalid window
            while (windowsize - max_freq) > k:
                #shrink window
                freq[s[l]] -= 1
                l += 1
                windowsize = r-l+1

            res = max(res,windowsize)
        return res