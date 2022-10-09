class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i) # for odd length palidrome, pointers start from same place i, i
            res += self.countPali(s, i, i + 1) # for even length palindrome, pointers start from adjacent places i.e. i, i+1
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: # check if the pointers are inbound and the values are same
            res += 1
            l -= 1
            r += 1
        return res
    
    