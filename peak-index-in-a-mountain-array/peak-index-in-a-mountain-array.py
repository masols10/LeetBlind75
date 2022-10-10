class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_element = float('-inf')
        max_index = -1
        for i in range(1, len(arr)-1):
            if arr[i] > max_element:
                max_element = arr[i]
                max_index   = i
        return max_index
            