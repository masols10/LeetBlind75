class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet: #checks if consecutive left element is present or not
                length = 1
                while (n + length) in numSet: #checks for consecutive elements along the len
                    length += 1
                longest = max(length, longest)
        return longest