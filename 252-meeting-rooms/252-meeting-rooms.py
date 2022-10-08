class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time complexity - O(nlogn) and space complexity - O(1)
        intervals.sort()
        for i in range(len(intervals) - 1): # iterate starting from index 1
            if intervals[i][1] > intervals[i + 1][0]: # when start time of current interval is less than the end time of previous interval they overalap
                return False
        return True
