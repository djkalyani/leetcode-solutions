class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def start_index(nums,target):
            #search left
            low,high = 0,n-1
            start = -1
            while low<=high:
                mid = low+(high-low)//2
                
                if nums[mid]>target:
                    high = mid-1
                elif nums[mid]<target:
                    low = mid+1
                else:
                    start = mid
                    high = mid - 1

            return start

        def end_index(nums,target):
            #search right 
            low,high = 0,n-1
            end = -1
            while low<=high:
                mid = low+(high-low)//2
                
                if nums[mid]>target:
                    high = mid-1
                elif nums[mid]<target:
                    low = mid+1
                else:
                    end = mid       
                    low = mid+1  #at one point the low>high then the last occured end value is taken
                                   #similarly for start index also 
            return end

        start = start_index(nums,target)
        end = end_index(nums,target)

        return [start,end]
                

