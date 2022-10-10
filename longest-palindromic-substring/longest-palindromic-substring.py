class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time complexity - O(n^2), space complexity- O(1), Brute force it is O(N^3)
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            # we are moving the pointers outwards starting from middle letter
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1] # update the res
                    resLen = r - l + 1
                l -= 1 
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
        '''
        def longestPalindrome(self, s: str) -> str:
            if s is '': 
                return s
            max_len = 0 
            start, end = 0, 0
            for i in range(len(s)):
                len1 = self.expandFromCenter(s, i, i)
                len2 = self.expandFromCenter(s, i, i+1)
                l = max(len1, len2)
                if l > end - start:
                    start = i - (l - 1) // 2
                    end = i + l // 2

        return s[start:end+1]

        def expandFromCenter(self, s, idx1, idx2):
            while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
                idx1 -= 1
                idx2 += 1
            return idx2 - idx1 - 1 
        '''