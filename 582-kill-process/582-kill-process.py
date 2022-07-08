class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(ppid)):
            process = pid[i]
            parent = ppid[i]
            graph[parent].append(process) 
        
        children = []
        
        def dfs(node):
            children.append(node)
            for child in graph[node]:
                dfs(child)
        
        dfs(kill)
        return children