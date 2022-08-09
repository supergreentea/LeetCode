class Solution:
    """
    |-------|
        |--------|
    
    |---------|
       |----|
    
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x : (x[0], x[1]))
        merged = [intervals[0]]
        for interval in intervals:
            prev_start, prev_end = merged[-1][0], merged[-1][1]
            cur_start, cur_end = interval[0], interval[1]
            if cur_start > prev_end:
                merged.append(interval)
            else:
                merged[-1][1] = max(cur_end, prev_end)
        return merged