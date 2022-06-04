class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)
        
        intervals.sort(key = lambda x: x[0])
        
        heapq.heappush(rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        
        return len(rooms)