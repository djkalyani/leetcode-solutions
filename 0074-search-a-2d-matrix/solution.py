class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        low, high = 0, n*m-1

        # treat matrix as a 1D array only 
        while low<=high:
            mid = low+(high-low)//2

            row = mid // m
            col = mid % m

            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low = mid+1
            else:
                high = mid-1

        return False
        
    '''   
        def findElementRow(matrix,col,target):
            left, right = 0, n-1
            while left<=right:
                mid = left+(right-left)//2
                if matrix[mid][col] > target:
                    left = mid+1
                elif matrix[mid][col] < target:
                    high = mid+1
                else:
                    return mid
            return mid'''
            
        

