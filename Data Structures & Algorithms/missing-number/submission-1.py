class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor 
        
        ans = len(nums)

        for i in range(len(nums)):
            ans ^= i ^ nums[i]

        return ans


        