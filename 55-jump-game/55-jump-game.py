class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy approach T-O(n), S- O(1) no extra space required
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1): # we traverse nums in reverse from end to start 
            if i + nums[i] >= goal: # once we reach the goal we move the goal left
                goal = i # move goal to left i.e where i was
        return goal == 0 # if the goal is 0 i.e we reach the goal, then we return True else False