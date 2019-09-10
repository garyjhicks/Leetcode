class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]
        for i in range(amount):
            dp.append(math.inf)

        for total in range(1, amount+1):
            for coin in coins:
                if total>=coin:
                    dp[total] = min(dp[total], dp[total-coin]+1)
        
        return -1 if dp[amount] == math.inf else dp[amount]
