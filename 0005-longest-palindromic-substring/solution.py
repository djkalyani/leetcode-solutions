class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        longest = s[0]
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    longest = substr if len(longest)<len(substr) else longest
        return longest
