    
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            
    # Bit manipulation solution
        res = 0
            for num in nums:
                res = res ^ num #XOR of same number results in 0 and the remaining number will be the single number
            return res
