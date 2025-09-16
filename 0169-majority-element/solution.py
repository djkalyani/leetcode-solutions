class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            dict1[i] = 0
        for i in nums:
            dict1[i]+=1
            if dict1[i]>(len(nums)//2):
                return i
        

        
