class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reversed_graph = defaultdict(list)
        indegree = defaultdict(int) # indegree after reversing edges

        for node in range(len(graph)):
            indegree[node] = len(graph[node])
            for neighbor in graph[node]:
                reversed_graph[neighbor].append(node)

        zero_indegree = []
        for node in range(len(graph)):
            if indegree[node] == 0:
                zero_indegree.append(node)

        safe_nodes = [False] * len(graph)

        while zero_indegree:
            node = zero_indegree.pop()
            safe_nodes[node] = True
            for neighbor in reversed_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree.append(neighbor)

        output = []
        for node in range(len(graph)):
            if safe_nodes[node]:
                output.append(node)

        return output