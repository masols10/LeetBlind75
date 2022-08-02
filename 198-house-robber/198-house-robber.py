class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top-down implementation T- O(n)
        def dp(i):
            # Base cases
            if i == 0: 
                return nums[0]            
            if i == 1: 
                return max(nums[0], nums[1])            
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i]) # Recurrence relation
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)
    '''
        # Bottom - up approach T- O(n), everything is the same, except that we use an array instead of a hash map and we iterate using a for-loop instead of using recursion
        
        if len(nums) == 1: 
            return nums[0]
        
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # Recurrence relation
        
        return dp[-1]   '''