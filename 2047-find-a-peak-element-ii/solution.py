class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)        # row
        m = len(mat[0])     # column

        def findRow(mat,col):
            maxVal = float('-inf')
            index = -1
            for i in range(n):
                if mat[i][col]>maxVal:
                    maxVal = mat[i][col]
                    index = i
            return index

        low, high = 0, m-1  # search b/w 0 to m-1 columns

        while low<=high:

            mid = low+(high-low)//2    # taking the centre column
            row = findRow(mat,mid)       # finding the row with max value in the mid-column

            left = mat[row][mid-1] if mid-1 >= 0 else -1
            right = mat[row][mid+1] if mid+1 < m else -1

            if left < mat[row][mid] and right < mat[row][mid]:
                return [row,mid]
            elif left > mat[row][mid] :
                high = mid-1    # if left value is greater --> move left
            else:
                low = mid+1     # if right value is greater --> move right
        
        return [-1,-1]

                








        

        '''
        def findColumn(mat,i,j):
            if mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i][j+1] and mat[i][j]>mat[i-1][j]:
                return True
            return False
        
        for i in range(len(mat)):
            low, high = 0, len(mat[0])
            while(low<=high):
    
                mid = (low+high) // 2

                result = findColumn(mat,i,mid)
                if result:
                    return [i,mid]
                
                if mat[i][mid]<mat[i][mid+1]:
                    low = mid+1
                elif mat[i][mid]>mat[i][mid+1]:
                    high = mid-1
        
        '''

