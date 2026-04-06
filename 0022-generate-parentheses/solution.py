class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # recursion
        def dfs(left,right,s):
            if left==right==n: # or - if len(s)==2*n  2 bcoz ( and )
                res.append(s)
                return
            if left<right:
                return
            if left < n:
                dfs(left+1,right,s+"(")
            if right < n:
                dfs(left,right+1,s+")")
            
        res = []
        dfs(0,0,"")
        return res
        


        '''
        iterative
        res=[]
        stack = [(0,0,'')]

        while stack:

            left, right, s = stack.pop()
            if len(s)==2*n:
                res.append(s)
                continue
            if left < n:
                stack.append((left+1,right,s+"("))
            if right < left:
                stack.append((left,right+1,s+")"))
        return res
        '''

