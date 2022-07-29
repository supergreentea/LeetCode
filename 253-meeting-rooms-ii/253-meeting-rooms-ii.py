class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        
        rooms = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_end = rooms[0]
            if cur_start >= prev_end:
                heappop(rooms)
            heappush(rooms, cur_end)
        
        return len(rooms)
        