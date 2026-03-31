class Solution:
    def diff(self,freq):
        maxVal = max(freq.values())
        minVal = min(freq.values())
        return maxVal-minVal
    def beautySum(self, s: str) -> int:
        total=0
        freq = {}
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                freq[s[j]]=freq.get(s[j],0)+1
                if len(freq)>=2:
                    total+=self.diff(freq)
            freq.clear() # freq only for a one substring
        return total

