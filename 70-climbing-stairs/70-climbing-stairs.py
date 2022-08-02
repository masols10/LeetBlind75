class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''def __init__(self):
		self.memo = {1: 1, 2: 2}

        def climbStairs(self, n: int) -> int:
            if n not in self.memo:
                self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n] '''
        
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    
    
        '''
        total = {}
        total[0] =0
        total[1] = 1
        total[2]= 2
        for i in range(3,n+1):
            total[i] = total[i-1]+ total[i-2]
        return total[n]
        '''