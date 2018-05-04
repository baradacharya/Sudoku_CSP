class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin] + 1)
        return dp[-1] if dp[-1] <= amount else -1