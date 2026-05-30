class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(',']':'[','}':'{'}

        for c in s:
            #got a closing Bracket
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:#got an opening Bracket
                stack.append(c)
        return not stack

