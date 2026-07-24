class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = dict()
        l, res = 0, 0
        
        for r in range(len(s)):

            if s[r] in charDict:
                l = max(charDict[s[r]]+1, l)
            
            charDict[s[r]] = r
            res = max(res,r-l+1)

        return res
