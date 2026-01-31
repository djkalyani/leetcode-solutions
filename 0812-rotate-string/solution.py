class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        '''if len(s)!= len(goal):
            return false
        for i in range(len(s)):
            for j in range(len(s)):
                temp = s[0]
                s[j] = s[j+1]
                a[len(s)-1] = temp
                if s== goal:
                    return true
        return false'''
        if len(s)!=len(goal):
            return False
        if goal in s+s:
            return True
        return False
