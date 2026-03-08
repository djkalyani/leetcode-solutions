class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        res = ""
        n = len(nums)
        for i in range(n):
            if nums[i][i]=='0':
                res+="1"
            else:
                res+="0"
        return res

        '''
        decimal_nums = []
        bin_till = "1"*len(nums[0])

        for i in range(len(nums)):
            decimal = int(nums[i],2)
            decimal_nums.append(decimal)

        for i in range(int(bin_till,2)+1):
            if i not in decimal_nums:
                unique = f"{i:0{len(nums[0])}b}"
        
        return unique
        '''
