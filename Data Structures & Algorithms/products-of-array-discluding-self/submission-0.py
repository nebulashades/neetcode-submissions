class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = 0
        z_idx = -1
        n = len(nums)
        prod = 1

        for i in range(n):
            if nums[i]==0:
                zeros+=1
                z_idx = i
            else:
                prod*=nums[i]
        
        res = [0]*n
        if zeros == 1:
            res[z_idx]= prod
        elif not zeros:
            for i in range(n):
                res[i]=prod//nums[i]

        return res
