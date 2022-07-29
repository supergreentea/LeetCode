class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # sort by gain company gets by sending person to city A instead of city B
        costs.sort(key = lambda cost : cost[0] - cost[1])
        
        total = 0
        n = len(costs) // 2
        
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        
        return total