class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
       
        def canWeMakeBouquet(bloomDay,m,k,day):
            flowers=0
            total=0 # no of bouquets

            for f in bloomDay:
                if f <= day:
                    flowers+=1
                    if flowers==k:
                        total+=1
                        flowers = 0
                else:
                    flowers=0
                
            if total>=m:
                return True
            return False
        
        low, high = 0, max(bloomDay)
        # we are not searching the array, we are searching the range 0->max(bloomDay) for the min day

        while low<high:
            mid = (low+high) //2
            
            if canWeMakeBouquet(bloomDay,m,k,mid):
                high=mid # if can do in mid days check for days<mid 
            else:
                low=mid+1
        
        return low


