class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preHash = {}
        preHash[0]=1
        preSum = 0
        cnt = 0
        for i in range(n):
            preSum+=nums[i]
            before = preSum - k
            if before in preHash:
                cnt+=preHash[before]
            if preSum in preHash:
                preHash[preSum]+=1
            else:
                preHash[preSum] = 1
        return cnt


        ''' meee
        n = len(nums)
        freq = 0
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum=sum+nums[j]
                if sum == k:
                    freq+=1
                j+=1
        return freq
        '''
         
        
        
