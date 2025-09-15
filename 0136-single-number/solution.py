class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            dict1[i]=0
        for i in nums:
            dict1[i]+=1
        for i in nums:
            if dict1[i]!=2:
                return i
