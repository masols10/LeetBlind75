class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Recursive solution, Brute force 
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1) '''
    
        # DP Bottom up approach 
        row = [1] * n # initialize all values in the last row to 1

        for i in range(m - 1): # need to iterate till the first row
            newRow = [1] * n
            for j in range(n - 2, -1, -1): # iterate backward leaving the last column which is always 1
                newRow[j] = newRow[j + 1] + row[j] # value will be right cell + bottom cell
            row = newRow
        return row[0] # we need the final value of all possible paths which is row[0]

        # O(n * m) O(n)