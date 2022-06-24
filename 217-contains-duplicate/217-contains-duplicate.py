class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            #check if the number exists first in the hasset and then add to the set
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    #Brute Force - T-O(n^2), S-O(1)
    #Sorting - T-O(nlogn), S-O(1)
    #Hash set -T-O(n), S-O(n) for creating n input hashset