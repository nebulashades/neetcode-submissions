class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        reach = [ 0 for i in range(n)]

        reach[0] = cost[0]
        reach[1] = cost[1]

        for i in range(2, n):
            reach[i] = min(cost[i]+reach[i-1], cost[i]+reach[i-2])

        return min(reach[n-1], reach[n-2])




        

        