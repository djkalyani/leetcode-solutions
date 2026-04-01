class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s1 = s.strip()
        s2 = s1.split()
        s1 = s2[::-1]
        for i in s1:
            i = i.strip()
        s2 = " ".join(s1)
        return s2
        '''
        print(s.split())
        print(s.split()[::-1])
        return ' '.join(s.split()[::-1])

