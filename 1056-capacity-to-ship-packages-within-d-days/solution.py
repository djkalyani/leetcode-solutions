class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        def possible(weights,days,minWeight):
            day_count = 1
            current_wt = 0
            for w in weights:
                current_wt+=w
                if current_wt > minWeight:
                    day_count+=1
                    current_wt=w
            if day_count<=days:
                return True
            return False
    
        low, high = max(weights),sum(weights)    
        while low<high:
            mid = (low+high)//2
            if possible(weights,days,mid):
                high = mid
            else:
                low = mid+1
        return low
