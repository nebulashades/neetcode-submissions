class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_p = nums[0]
        min_p = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            temp = max_p
            max_p =  max(nums[i], max_p*nums[i], min_p*nums[i])
            min_p =  min(nums[i], temp*nums[i], min_p*nums[i])
            ans = max(max_p, ans)

        return ans

            


        