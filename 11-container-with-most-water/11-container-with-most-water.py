class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force T-O(n^2), S-O(1)
        '''maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea
        '''
        #Two pointer approach T-O(n), S-O(1)
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea