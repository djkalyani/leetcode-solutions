class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0,x
        ans  = -1

        while low<=high:
            mid = (low+high)//2
            val = mid*mid

            if val == x:
                return mid
            
            elif val>x:
                high=mid-1
            
            else:
                low = mid+1
                ans = mid
        
        return ans
