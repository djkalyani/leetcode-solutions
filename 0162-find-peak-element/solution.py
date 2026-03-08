class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low,high = 0,n-1
        
        # edge cases - first and last elements
        if n==1:
            return 0

        if nums[0]>nums[1]:
            return 0
        
        if nums[n-1]>nums[n-2]:
            return n-1

        while low<=high:
            mid = low + (high-low)//2
            # check if mid is peak element
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            
            # slopes guarenteed because array ends at -inf. so if no peak, last element will be peak
            #ascending slope -> move right - eliminate left half
            if nums[mid]<nums[mid+1]:
                low = mid + 1
            
            #descending slope -> move left
            if nums[mid]>nums[mid+1]:
                high = mid-1

            
