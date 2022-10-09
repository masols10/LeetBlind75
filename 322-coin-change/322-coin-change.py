class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # initialize default dp array to amount + 1
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # recurrence relation e.g a= 7 and c = 3 --> we find dp[7-3] i.e dp[4]
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    # Time complexity is O(amount * len(coins))
    # Space complexity is O(amount)