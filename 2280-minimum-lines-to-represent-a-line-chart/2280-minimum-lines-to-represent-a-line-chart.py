class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key = lambda x : x[0])
        if len(stockPrices) <= 1:
            return 0
        
        prev_x, prev_y = stockPrices[0]
        cur_x, cur_y = stockPrices[1]
        
        lines = 1
        
        for i in range(2, len(stockPrices)):
            new_x, new_y = stockPrices[i]
            
            if (new_y - cur_y) * (cur_x - prev_x) != (new_x - cur_x) * (cur_y - prev_y):
                lines += 1
            
            prev_x, prev_y, cur_x, cur_y = cur_x, cur_y, new_x, new_y
        
        return lines
            
            