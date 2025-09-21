class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        S = [0]*150
        T = [0]*150

        for i in range(len(s)):
            if S[ord(s[i])]!=T[ord(t[i])]:
                return False
            S[ord(s[i])] = i+1
            T[ord(t[i])] = i+1
        return True
