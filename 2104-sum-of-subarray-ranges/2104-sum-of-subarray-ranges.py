class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0 
        
        for i in range(len(nums)):
            largest, smallest = nums[i], nums[i]
            for j in range(i+1, len(nums)):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                ans += largest - smallest 
                
        return ans