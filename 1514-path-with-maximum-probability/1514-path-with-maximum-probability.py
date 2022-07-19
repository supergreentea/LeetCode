class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        G = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            G[a].append((b, prob))
            G[b].append((a, prob))
        
        max_probability = [0 for node in range(n)]
        max_probability[start] = 1
        
        PQ = []
        heappush(PQ, (-1, start))
        while PQ:
            pro, node = heappop(PQ)
            pro *= -1
            if pro < max_probability[node]: continue
            for nbr, w in G[node]:
                if pro * w > max_probability[nbr]:
                    max_probability[nbr] = pro * w
                    heappush(PQ, (-pro * w, nbr))
        return max_probability[end]