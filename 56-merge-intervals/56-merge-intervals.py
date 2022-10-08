class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]] #First interval

        for start, end in intervals:
            lastEnd = output[-1][1] # end value of most recently added interval output[-1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end) # we have to take the max of end values of intervals
            else:
                output.append([start, end])
        return output