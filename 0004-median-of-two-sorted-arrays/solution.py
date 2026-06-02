
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        m=len(nums1)
        n=len(nums2)

        for i in range(m):
            arr.append(nums1[i])
        for j in range(n):
            arr.append(nums2[j])
        arr.sort()

        length=len(arr)
        if (length)%2==1:
            return arr[length//2]
        else:
            median_index = length//2
            return (arr[median_index]+arr[median_index-1])/2
