class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] # set the default to the first value as the array can have negative elemenst too and it cant be 0, will have a value

        total = 0
        for n in nums:
            total += n # we add current value to the current sum, this makes sure we are computing the max we can 
            res = max(res, total)
            if total < 0: # if the total is less than 0, we set the total to 0 and start over
                total = 0
        return res
    
    '''
    1) Initialize 2 integer variables. Set both of them equal to the first value in the array.
            *currentSubarray will keep the running count of the current subarray we are focusing on.
            *maxSubarray will be our final return value. Continuously update it whenever we find a bigger subarray.
    2) Iterate through the array, starting with the 2nd element (as we used the first element to initialize our variables). For each number, add it to the                  currentSubarray we are building. If currentSubarray becomes negative, we know it isn't worth keeping, so throw it away. Remember to update maxSubarray every        time we find a new maximum.
    3)Return maxSubarray.
    
    def maxSubArray(self, nums: List[int]) -> int:
    # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray'''
    
