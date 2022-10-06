#Brute Force approach : T:O(n^3), S: O(min(n,m))
#Sliding window approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0  #left pointer and right pointer is moving(r)
        res = 0 # initial result 
        
        for r in range(len(s)):
            while s[r] in charSet: # if it coes across a duplicate, remove the leftmost char and update left pointer to +1 
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) # after removing all duplicates we add rightmost char to our set
            res = max(res, r - l + 1) # update result using current window length
        return res
    
    Time complexity : O(n)
    Space complexity : O(m)
