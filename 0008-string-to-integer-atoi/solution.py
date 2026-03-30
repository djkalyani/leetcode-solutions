class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()  # remove leading spaces only
        if not s:
            return 0
        sign, i = 1, 0
        if s[0]=='-':
            sign = -1
            i+=1
        elif s[0]=='+':
            i+=1
        num = 0
        while i<len(s) and s[i].isdigit():
            digit = int(s[i])
            # num*10+digit<=INT_MAX --> num> (int_max-digit)//10 by rearranging inequality
            if num > (2**31-1-digit)//10:
                return -2**31 if sign==-1 else 2**31-1
            num=num*10+digit
            i+=1
        
        return sign*num



        '''
        s = s.replace(" ","") # removing spaces
        num = ""
        neg = False
        start=0
        if s[0].isalpha():
            return 0
        if s[0]=="-":   
            neg = True
            start=1
        elif s[0]=="+":
            start = 1
        for i in range(start,len(s)):
            if s[i].isdigit():
                num+=s[i]
            else:
                break
        
        if neg:
            return -1*int(num)
        else:
            return int(num)
        
        '''

            

        



