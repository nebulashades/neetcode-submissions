class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []
        n=len(height)

        max_ele=height[0]

        for i in range(n):
            if height[i]>max_ele:
                max_ele=height[i]
            prefix.append(max_ele)

        max_ele=height[-1]
        suffix = [0]*n

        for i in range(n-1, -1, -1):
            if height[i]>max_ele:
                max_ele=height[i]
            suffix[i]= max_ele

        trap = 0

        for i in range(n):
            trap += min(prefix[i], suffix[i]) - height[i]
        
        return trap



        