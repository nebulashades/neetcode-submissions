class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        no = [amount+1 for i in range(amount+1)]

        no[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if coin <= amt:
                    rest_amt = amt - coin
                    no[amt] = min(no[amt], 1+no[rest_amt])

        if no[amount] <= amount:
            return no[amount]

        return -1




        