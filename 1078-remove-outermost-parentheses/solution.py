class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        level = 0
        result=""
        for p in s:
            if p=="(":
                level+=1
                if level>1:
                    result+="("
            if p==")":
                level-=1
                if level>0:
                    result+=")"
        
        return result
