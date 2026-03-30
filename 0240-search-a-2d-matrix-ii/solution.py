class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
        n,m = len(matrix), len(matrix[0])
        # starting from top-right corner
        i,j = 0,m-1     
        # from top-right
            # left --> smaller values
            # down --> bigger values
        while i<n and j>=0:
            if matrix[i][j] == target:
                return True
            # smaller value --> move left
            elif target < matrix[i][j]:     
                j-=1
            # bigger values --> move down
            else:
                i+=1
        return False

        
        '''
        def findRow(matrix,col,target):
            left, right = 0, n-1
            while left<=right:
                mid = left+(right-left)//2

                if matrix[mid][col] == target:
                    return mid
                elif matrix[mid][col] < target:
                    left = mid+1
                else:
                    right = mid-1
            return left



        low, high = 0, m-1
        while low<=high:
            mid = low+(high-low)//2
            row = findRow(matrix,mid,target)

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid+1
            else:
                high = mid-1
        return False
        '''
