class Solution:
    def beautySum(self, s: str) -> int:
        '''
        n = len(s)

        char_count = Counter(s)
        frequency = []
        for c in char_count.values():
            frequency.append(c)
        
        print(frequency)
        return (max(frequency)-min(frequency))
        
        '''

        n = len(s)
        total=0
        for i in range(n):
            freq = {}
            for j in range(i,n):
                freq[s[j]]=freq.get(s[j],0)+1

                values = freq.values()
                maxVal = max(values)
                minVal = min(values)

                total+= maxVal-minVal
            
        return total
