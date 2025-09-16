class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = nums.count(0)
        c1 = nums.count(1)
        for i in range(len(nums)):
            if i<c0:
                nums[i] = 0
            elif i< c0+c1:
                nums[i] = 1
            else:
                nums[i] = 2











        '''
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        for i in range(c0):
            nums.remove(0)
            nums.append(0)
        for j in range(c1):
            nums.remove(1)
            nums.append(1)
        for k in range(c2):
            nums.remove(2)
            nums.append(2)
        '''
        
