class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0], x[1]))
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev_start, prev_end = output[-1]
            start, end = intervals[i]
            if start > prev_end:
                output.append([start, end])
            else:
                output.pop()
                output.append([prev_start, max(prev_end, end)])
        
        return output