class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # row[] --> matrix[][0] - col -- n
        # col[] --> matrix[0] - row -- m
 
        col0 = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j!=0:  #that col0 extra
                        matrix[0][j]=0
                    else:
                        col0 = 0

        #changing other than the 1st col and row
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] != 0:
                    if matrix[i][0]==0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        #checking for the 1st row and col elements. Do the row first
        if matrix[0][0] == 0:
            for j in range(n):  #change the first row's columns
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(m):   #changing the first column's row
                matrix[i][0] = 0
