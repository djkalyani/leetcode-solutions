class Solution:
    def maxDepth(self, s: str) -> int:
        level = 0
        max = 0
        for c in s:
            if c == "(":
                level+=1
                if max<level:
                    max = level
            if c == ")":
                level-=1
        return max
