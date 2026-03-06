class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        flag = 0

        count1 = s.count('1')
        print(count1)
        for i in range(count1):
            if s[i]=='0':
                print(s[i])
                return False
            
        return True

            
