class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        count1=0 #startting with 101010...
        count0=0 # 010101...
        for i in range(n):
            if i%2==0:
                if s[i]!='0':
                    count0+=1
                if s[i]!='1':
                    count1+=1
            else:
                if s[i]!='1':
                    count0+=1
                if s[i]!='0':
                    count1+=1
        return min(count0,count1)

       

