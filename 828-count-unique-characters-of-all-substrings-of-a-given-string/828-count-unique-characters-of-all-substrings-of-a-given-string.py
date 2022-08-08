'''Brute Force:
-- O(N^2), you keep one set called visited, and one set called duplicate

Key Idea:
-- Find aggregate subarray by element, instead of reaching each subarray and iterate through each case

Key Point:

For each element inside an subarray, find its total contribution to the uniqueCount(A.K.A for an element inside an unique subarray, how many times it will be counted)

Product Rule:
-- For any element at index i inside an unique subarray, it will be counted for

(i - j)*(k - i), where j is the LAST position that the element appears, k is the NEXT position that the element appears
Question: What if the element only shows once?
j == -1, k == len(s)
Example:
A B C D
C will be counted for (2 - (-1))*(4 - 2) = 6 times
Implementation Detail:

Construct an 2D array, where len(array) = 26, and len(array[i]) depends on how many times that char appears.
For each letter, we append -1 into its bucket(A.K.A: array[i]).
Iterate through the s, append the index of each letter into its bucket when it is appeared.
For each letter, we append n into its bucket.
Iterate through 26 letters, and calculate the contributions of each letter by using Product Rule.
Time Complexity:
O(N) -- O(26) * 2 + O(2*N)

Space Complexity:
O(N) '''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        
        #Step1
        appear_Index = [[] for _ in range(26)]
        
        
        #Step2 - Step4
        for i in range(26):
            appear_Index[i].append(-1)
        for idx, char in enumerate(s):
            index = ord(char) - ord("A")
            appear_Index[index].append(idx)
        for i in range(26):
            appear_Index[i].append(len(s))
            
        #Step5
        output = 0
        for i in range(26):
            bucket = appear_Index[i]
            
            #Because -1 & n are virtual indices, we dont want to include them
            for j in range(1, len(bucket) - 1):
                cnt = (bucket[j] - bucket[j - 1])*(bucket[j + 1] - bucket[j])
                output += cnt
        
        return output