class Solution:
    # optimal - Binary Search
    # total hrs reqd to eat all in the given speed 'hourly'



    def calculateHours(self,piles,hourly):
        total_hrs=0
        for pile in piles:  
            total_hrs += ceil(pile/hourly)
        return total_hrs

    # min eating spped
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        hours = max(piles)
        while low<=high:
            mid = (low+high)//2
            minHours = self.calculateHours(piles,mid)
            if minHours<=h:
                hours=mid
                high=mid-1
            else:
                low=mid+1
        return low


