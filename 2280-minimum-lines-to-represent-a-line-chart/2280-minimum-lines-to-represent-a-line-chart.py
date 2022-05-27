class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) < 2:
            return 0
        res = 1
        stockPrices.sort(key = lambda x: x[0])
        # a / b = c / d <= > a * d = b * c
        
        delta_x, delta_y = stockPrices[1][0] - stockPrices[0][0], stockPrices[1][1] - stockPrices[0][1]
        
        for i in range(2, len(stockPrices)):
            delta_x_prime, delta_y_prime = stockPrices[i][0] - stockPrices[i - 1][0], stockPrices[i][1] - stockPrices[i - 1][1]
            if delta_x_prime * delta_y != delta_y_prime * delta_x:
                res += 1
                delta_x, delta_y = delta_x_prime, delta_y_prime
        return res
            
        