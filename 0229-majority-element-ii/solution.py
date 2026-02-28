class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        maj_ele = []
        n=len(nums)
        target = n//3
        
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            if freq[nums[i]] == target+1:
                maj_ele.append(nums[i])
            
        
        return maj_ele
        

