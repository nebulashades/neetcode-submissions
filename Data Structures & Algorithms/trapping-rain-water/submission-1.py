class Solution:
    def trap(self, height: List[int]) -> int:

        # Using 2 pointers 

        l_max=height[0]
        left = 0
        right = len(height)-1
        r_max=height[-1]

        trap = 0

        while left < right:
            if height[left] > l_max:
                l_max=height[left]
            if height[right] > r_max:
                r_max=height[right]
                
            if height[left] < height[right]:
                trap += min(l_max, r_max) - height[left]
                left+=1                                     
            else:
                trap += min(l_max, r_max) - height[right]
                right-=1

        return trap



        