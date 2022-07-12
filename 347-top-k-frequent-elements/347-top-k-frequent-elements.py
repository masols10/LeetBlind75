class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort - O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        for n, c in count.items(): #count is the key and values are the numbers
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # Descending order i.e right to left
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        ''' nums = [1,1,1,2,2,100]
        Bucketing
        i(count) 0  1    2    3   4   5   6  Start checing from max count right to left
        values    [100] [2]  [1]             '''
        # Heap - O(klogn)