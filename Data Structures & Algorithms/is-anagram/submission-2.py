class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkbook = dict()
        for i in s:
            if i not in checkbook:
                checkbook[i] = 1
            else:
                checkbook[i] += 1

        for j in t:
            if j not in checkbook:
                return False
            checkbook[j] -=1
        
        return all(value == 0 for value in checkbook.values())