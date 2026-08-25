class Solution:
    def rob(self, nums: List[int]) -> int:

        # 2 1 1 2
        # 2 2 3 4
        #    p2 p1 

        # 1 1 3 2
        # 1 1 4 4


        n=len(nums)
        if n==1:
            return nums[0]

        p2 = nums[0] 
        p1 = max(nums[0], nums[1])

        for i in range(2, n):
            temp = max(p2 + nums[i], p1)
            p2 = p1
            p1 = temp 
            
        return p1



        
