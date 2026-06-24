class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1map = {}
        windowmap = {}

        for i in range(n1):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1
            windowmap[s2[i]] = windowmap.get(s2[i], 0) + 1
        
        if s1map == windowmap:
            return True
        
        for i in range(n1, n2):
            #right char entering
            rightchar = s2[i]
            windowmap[rightchar] = windowmap.get(rightchar, 0) + 1

            #left char leaving
            leftchar = s2[i - n1]
            windowmap[leftchar] -= 1

            if windowmap[leftchar] == 0:
                del windowmap[leftchar]

            if windowmap == s1map:
                return True
        return False
            
            
            
