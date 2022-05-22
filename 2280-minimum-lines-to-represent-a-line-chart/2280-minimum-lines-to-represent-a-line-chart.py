from fractions import Fraction

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x: x[0])
        if len(stockPrices) < 2:
            return 0
        lines = 1
        prevSlope = Fraction((stockPrices[1][1] - stockPrices[0][1]), (stockPrices[1][0] - stockPrices[0][0]))
        for i in range(2, len(stockPrices)):
            slope = Fraction((stockPrices[i][1] - stockPrices[i - 1][1]), (stockPrices[i][0] - stockPrices[i - 1][0]))
            if prevSlope != slope:
                lines += 1
                prevSlope = slope
        return lines
        