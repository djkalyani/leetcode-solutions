class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dict1:
                return [dict1[other],i]
            else:
                dict1[nums[i]]=i
        return []

       
       
       
       
       
       
       
       
       
        '''
        n = nums
        nums = sorted(nums)
        begin = 0
        end = len(nums)-1
        while(begin<end):
            if (nums[begin]+nums[end])==target:
                nxt = n.index(nums[begin])
                return [n.index(nums[begin]),n.index(nums[end],nxt+1)]
            elif (nums[begin]+nums[end])>target:
                end-=1
            else:
                begin+=1
        return []
        '''  
