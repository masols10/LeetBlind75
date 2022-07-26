class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p - 1) // m) + 1
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k'''
    
    
        #2
        l, r = 1, max(piles)
        res = r #max in piles, this atleast will work we need minima
        
        while l <= r:
            k =(l + r) // 2
            hours = 0
            for p in piles:
                hours += ceil(p / k) # ceil rounds off in python
                
            if hours <= h: # we are finding minimum in hours 
                res = min(res, k)
                r = k - 1 
            else:
                l = k + 1
             
        return res
                