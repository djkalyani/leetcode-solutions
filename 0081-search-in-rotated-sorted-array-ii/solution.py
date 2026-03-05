class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1
        nums.sort()
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return False
