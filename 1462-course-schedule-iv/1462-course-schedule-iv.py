class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        G = defaultdict(list)
        indegree = defaultdict(int)
        crs_to_prereqs = defaultdict(set)
        
        for pre, crs in prerequisites:
            G[pre].append(crs)
            crs_to_prereqs[crs].add(pre)
            indegree[crs] += 1
        
        zero_indegree = [crs for crs in range(numCourses) if indegree[crs] == 0]
        
        while zero_indegree:
            pre = zero_indegree.pop()
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_indegree.append(crs)
                crs_to_prereqs[crs].update(crs_to_prereqs[pre])
        
        answer = [(u in crs_to_prereqs[v]) for u, v in queries]
        return answer