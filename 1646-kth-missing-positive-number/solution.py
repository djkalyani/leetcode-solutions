class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #brute
        current=1
        i=0
        while k>0:
            if i<len(arr) and arr[i]==current:
                i+=1
            else:
                k-=1
                if k==0:
                    return current
            current+=1

        
        
        
        
        
        
        
        
        
        
        '''missing = []
        end = max(arr)
        count=0

        for i in range(1,end):
            if i not in arr:
                missing.append(i)
                count+=1

        return missing[k]'''
