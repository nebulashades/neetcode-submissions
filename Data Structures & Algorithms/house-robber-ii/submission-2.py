class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(start, end):

            p2 = nums[start]
            p1 = max(nums[start], nums[start+1])
             
            for i in range(start+2, end):
                temp = max(p2+nums[i], p1)
                p2 = p1
                p1 = temp

            return p1

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        skip_first = helper(1,n)
        with_first = helper(0,n-1)

        return max(skip_first, with_first)
        



        