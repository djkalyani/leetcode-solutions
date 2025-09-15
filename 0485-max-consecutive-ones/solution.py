class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        flag = 0
        max_con = 0
        c=0
        for i in nums:
            if flag==1 and i==1:
                c+=1
            elif i==1:
                c+=1
                flag=1
            else:
                flag = 0
                c=0
            if c>max_con:
                max_con = c
        return max_con'''
        res = 0
        cur = 0
        for n in nums:
            if n:
                cur += 1
                if cur > res:
                    res = cur
            else:
                cur = 0
        return res
