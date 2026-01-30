class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        spiral = []
        
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while top<=bottom and left<=right:
            #left --> right
            for i in range(left,right+1):
                spiral.append(matrix[top][i])
            top+=1

            #top --> bottom
            for j in range(top,bottom+1):
                spiral.append(matrix[j][right])
            right-=1

            #right --> left
            if top<=bottom:
                for k in range(right,left-1,-1):
                    spiral.append(matrix[bottom][k])
                bottom-=1

            #bottom --> top
            if left<=right:
                for l in range(bottom,top-1,-1):
                    spiral.append(matrix[l][left])
                left+=1

            print(top,bottom,left,right)
        
        return spiral


