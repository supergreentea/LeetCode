class UndergroundSystem:

    def __init__(self):
        self.checked_in = {}
        self.stations = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)    

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endStation = stationName
        arrival = t
        
        startStation, boarded = self.checked_in[id]
        
        
        total_time, count = self.stations.get((startStation, endStation), (0, 0))
        
        self.stations[(startStation, endStation)] = (total_time + arrival - boarded, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.stations[(startStation, endStation)]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)