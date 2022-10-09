class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # we dont consider 1st element and last element cause they will overalap, so run the helper on other frames
        
    def helper(self, nums):
        rob1, rob2 = 0, 0 #max rob that a house can give at a given point
        for n in nums:
            newRob = max((rob1 + n), rob2)
            rob1 = rob2
            rob2 = newRob
            
        return rob2
            