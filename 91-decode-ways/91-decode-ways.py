class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1} # memcache

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"): # checking if the the number lies between 10 and 26
                res += dfs(i + 2) # run recursive dfs on 2nd position
            dp[i] = res # add to cache
            return res

        return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1} 
        for i in range(len(s) - 1, -1, -1): # Bottom up approach - starting from the end of the string
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] # add to cache

            if i + 1 < len(s) and ( s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2] # add to cache
        return dp[0]