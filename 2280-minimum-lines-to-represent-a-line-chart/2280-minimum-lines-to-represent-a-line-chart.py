class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key = lambda x : x[0])
        if len(stockPrices) < 2:
            return 0
        if len(stockPrices) == 2:
            return 1
        
        lines = 1
        for i in range(1, len(stockPrices) - 1):
            if (stockPrices[i][0] - stockPrices[i-1][0]) * (stockPrices[i+1][1] - stockPrices[i][1]) != (stockPrices[i][1] - stockPrices[i-1][1]) * (stockPrices[i+1][0] - stockPrices[i][0]):
                lines += 1
        
        return lines