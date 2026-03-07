class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # edge cases
        if n==1:                    # when only one element in array
            return nums[0]
        elif nums[0]!=nums[1]:      # when 1st element - single
            return nums[0]
        elif nums[n-1]!=nums[n-2]:  # when last element - single
            return nums[n-1]

        # all other cases
        else:
            low, high = 1, n-2
            while low < high:
                mid = low + (high-low)//2

                # mid element is single
                if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                    return nums[mid]

                # even-odd pair --> element on right half
                if (mid%2!=0 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                    low = mid + 1
                
                # odd-even pair --> element on left side
                if (mid%2!=0 and nums[mid-1]!=nums[mid]) or (mid%2==0 and nums[mid]!=nums[mid+1]):
                    high = mid
                
        
        ''' brute
        n = len(nums)
        for i in range(n):
            count = nums.count(nums[i])
            if count == 1:
                return nums[i]
            else:
                i+=(count)
        '''

        
