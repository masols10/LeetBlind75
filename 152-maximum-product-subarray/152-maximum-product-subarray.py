class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1 # set default to 1 as it should atleast have 1

        for n in nums:

            tmp = curMax * n # to maintain the older curMax we store it in temp
            curMax = max(n * curMax, n * curMin, n) # taking curMax and curMin to take care of negative values too
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res