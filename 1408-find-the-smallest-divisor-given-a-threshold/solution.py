import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)


        def isPossibleDivisor(nums,threshold,div):
            total=0
            for num in nums:
                total+= ceil(num/div)
            
            if total<=threshold:
                return True
            return False
        
        low, high = 1,max(nums)
        while low<high:
            mid = (low+high)//2

            if isPossibleDivisor(nums,threshold,mid):
                high = mid
            else:
                low=mid+1
        
        return low
        
            

