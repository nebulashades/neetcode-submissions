class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
            if max_p < profit:
                max_p = profit
        return max_p
