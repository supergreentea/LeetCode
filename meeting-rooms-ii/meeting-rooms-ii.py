class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        rooms = []
        heapq.heapify(rooms)
        
        for start, end in intervals:
            if len(rooms) > 0 and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        
        return len(rooms)
                