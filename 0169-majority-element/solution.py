class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        dict1 = {}
        for i in nums:
            dict1[i] = 0
        for i in nums:
            dict1[i]+=1
            if dict1[i]>(len(nums)//2):
                return i
        
        '''
        '''
        my own logic
        dict1={}
        majority = floor(len(nums)/2)
        maj_element = -1
        for i in range(len(nums)):
            if nums[i] in dict1:
                cnt = dict1[nums[i]]
            else:
                cnt = nums.count(nums[i])
            if cnt>majority:
                dict1[nums[i]]=cnt
                majority = cnt
                maj_element = nums[i]
        return maj_element
        '''
        dict1={}
        for i in nums:
            dict1[i]=0
        for i in nums:
            dict1[i]+=1
            if dict1[i]>(len(nums)//2):
                return i
