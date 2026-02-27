class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for row in range(1,numRows+1):
            inner = []
            ans = 1
            inner.append(ans)
            for col in range(1,row):
                ans = ans*(row-col)
                ans = int(ans/col)
                inner.append(ans)
            pascal.append(inner)
        return pascal

