class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]

        dp = [0]*(n+1)
        dp[1]=1
        power = 4

        for i in range(2, n+1):
            if i < power:
                dp[i]=dp[i - (power//2)] + 1
            if i == power:
                power*=2
                dp[i]=1

        return dp


