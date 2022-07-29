class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.total_times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endStation, arrivalTime = stationName, t
        startStation, startTime = self.check_in_data[id]
        travelTime = arrivalTime - startTime
        totalTime, count = self.total_times.get((startStation, endStation), (0, 0))
        self.total_times[(startStation, endStation)] = totalTime + travelTime, count + 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.total_times[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)