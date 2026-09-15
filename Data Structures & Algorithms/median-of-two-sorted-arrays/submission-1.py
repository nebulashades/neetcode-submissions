class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m=len(nums1)
        n=len(nums2)

        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (len(nums1)+len(nums2))//2
        x = 0 

        while True:
            y = half - x
            x1 = nums1[x-1] if x>0 else float("-inf")
            x2 = nums1[x] if x<m else float("inf")
            y1 = nums2[y-1] if y>0 else float("-inf")
            y2 = nums2[y] if y<n else float("inf")            

            if x1 <= y2 and y1 <= x2:
                if (m+n)%2 == 0:
                    return (max(x1, y1)+min(x2, y2))/2
                else:
                    return min(x2, y2)

            elif x1 > y2:
                x-=1

            elif y1 > x2:
                x+=1


        