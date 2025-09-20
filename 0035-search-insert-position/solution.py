class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        '''
        if nums[mid]<target:
            mid+=1
        if mid<0:
            return 0
        return mid
        '''
        return low
