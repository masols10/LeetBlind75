class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Bottom up DP T-O(m*n), S-O(m*n) for the grid
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] #Initialize o grid with extra row and column

        for i in range(len(text1) - 1, -1, -1): # iterate from bottom i.e in reverse
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1] # if the charactes match consider the diagonal value
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]) # if the characters dont match consider the max of right or bottom value 

        return dp[0][0]










