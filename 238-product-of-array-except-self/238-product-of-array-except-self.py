class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # T- O(n) , S- O(1)
        # get product values of prefix elements and product values of postfix elements and                 multiply both. If we maintain them in lists it will take extra memory of O(n) so                 directly store prefix values in result list and get postfix values and multiply them             with the prefix elements already present in the list
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #reverse for loop
            res[i] *= postfix
            postfix *= nums[i]
        return res