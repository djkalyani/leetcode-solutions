class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0 
        for i in range(len(s)):
            current = values[s[i]]
            if i<len(s)-1:
                next = values[s[i+1]]
                if current<next:
                    number-=current
                else:
                    number+=current
            else:
                number+=current
            
        return number
        '''
        me brute force 15ms beats 5.10%
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        i = len(s)-1
        while(i>-1):
            value = dict1.get(s[i])
            if i>0:
                if (s[i]=="V" or s[i]=="X") and s[i-1]=="I":
                    value-=1
                    i-=1
                elif (s[i]=="L" or s[i]=="C") and s[i-1]=="X":
                    value-=10
                    i-=1
                elif (s[i]=="D" or s[i]=="M") and s[i-1]=="C":
                    value-=100
                    i-=1
            i-=1
            number+=value
        return number
        '''


