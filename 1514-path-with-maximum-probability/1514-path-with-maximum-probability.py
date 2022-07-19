class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        max_probability = defaultdict(int)
        max_probability[start] = 1
        
        PQ = []
        heappush(PQ, (-1, start))
            
        while PQ:
            prob, node = heappop(PQ)
            prob *= -1
            if prob < max_probability[node]: # we've already found a better path
                continue
            for neighbor, weight in graph[node]:
                if prob * weight > max_probability[neighbor]:
                    max_probability[neighbor] =  prob * weight
                    heappush(PQ, (-prob * weight, neighbor))
        return max_probability[end]