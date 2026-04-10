class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_word_count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                break
            else:
                last_word_count+=1
        return last_word_count
