class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)
        intervals.sort(key = lambda x : x[0])
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)