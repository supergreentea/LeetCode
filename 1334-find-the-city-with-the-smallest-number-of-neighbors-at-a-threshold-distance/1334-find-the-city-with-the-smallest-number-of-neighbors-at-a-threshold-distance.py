class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_neighbors = math.inf
        the_city = -1
        
        def get_neighbors_within_threshold(city):
            nonlocal min_neighbors
            nonlocal the_city 
            
            distances = { node : math.inf for node in range(n) }
            distances[city] = 0
            neighbors_within_threshold = 0
            
            PQ = [(0, city)]
            while PQ:
                cur_dist, cur_city = heappop(PQ)
                if cur_dist > distanceThreshold:
                    break
                if cur_dist > distances[cur_city]:
                    continue
                for neighbor, weight in graph[cur_city]:
                    new_dist = cur_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heappush(PQ, (new_dist, neighbor))
            
            for node, distance in distances.items():
                if node == city:
                    continue
                if distance <= distanceThreshold:
                    neighbors_within_threshold += 1
            
            if neighbors_within_threshold < min_neighbors:
                min_neighbors = neighbors_within_threshold
                the_city = city
            if neighbors_within_threshold == min_neighbors and city > the_city:
                the_city = city
        
        for city in range(n):
            get_neighbors_within_threshold(city)
        
        return the_city