class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []  

        def dfs(target, start):
            if target == 0:
                res.append(list(current))
            elif target < 0:
                return 

            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(target - nums[i], i)    
                current.pop() 

        dfs(target, 0)    

        return res   






