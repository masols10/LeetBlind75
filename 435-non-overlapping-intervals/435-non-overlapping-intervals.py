class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]: # start the loop from first index
            if start >= prevEnd: #if current start is greater than or equal to the previous end means they are non-ovelapping
                prevEnd = end
            else: #overlapping condition 
                res += 1
                prevEnd = min(end, prevEnd)
        return res