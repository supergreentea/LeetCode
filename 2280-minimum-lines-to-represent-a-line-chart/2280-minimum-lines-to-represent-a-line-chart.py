class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) < 2:
            return 0
        stockPrices.sort(key=lambda x: x[0])
        count = 1
        deltaX, deltaY = stockPrices[1][0] - stockPrices[0][0], stockPrices[1][1] - stockPrices[0][1]
        
        for i in range(2, len(stockPrices)):
            newDeltaX, newDeltaY = stockPrices[i][0] - stockPrices[i - 1][0], stockPrices[i][1] - stockPrices[i - 1][1]
            if deltaX * newDeltaY != deltaY * newDeltaX:
                count += 1
            deltaX, deltaY = newDeltaX, newDeltaY
        
        return count