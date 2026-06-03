class Solution:
    def isValid(self, s: str) -> bool:
        char = {'(':')','{':'}','[':']'}
        stack = list()
        for ch in s:
            if ch in char:
                stack.append(ch)
            elif ch in char.values():
                if stack:
                    c = stack.pop()
                    if char[c]!=ch:
                        return False
                else:
                    return False
            
        return len(stack)==0
