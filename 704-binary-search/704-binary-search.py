class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target: #when midpoint of sorted list is less than target, shift left pointer to m+1 i.e we are eliminating lesser values 
                l = m + 1
            else:
                return m
        return -1