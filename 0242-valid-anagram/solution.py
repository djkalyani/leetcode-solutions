class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        '''
        d = dict()
        di = dict()
        for k in s:
            d[k]=0
        for k in t:
            di[k]=0
        for i in s:
            d[i]+=1
        for j in t:
            di[j] += 1
        for i in s:
            if i not in t or d[i]!=di[i]:
                return False
        return True
        '''
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        for ch in t:
            d[ch] = d.get(ch,0)-1
        for count in d.values():
            if count!=0:
                return False
        return True
