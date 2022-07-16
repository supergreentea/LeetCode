class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or target in deadends:
            return -1
        
        if target == "0000":
            return 0
        
        start_queue = deque([("0000", 0)])
        end_queue = deque([(target, 0)])
        
        start_visited = { "0000" : 0 }
        end_visited = { target : 0 }
        
        def get_next_states(lock):
            output = []
            state = [int(char) for char in lock]
            for i in range(4):
                original = state[i]
                state[i] = (original + 1) % 10
                output.append("".join(map(str, state)))
                state[i] = (original + 10 - 1) % 10
                output.append("".join(map(str, state)))
                state[i] = original
            return output
            
        def bfs(queue, visited, other_visited):
            for _ in range(len(queue)):
                lock_state, turns = queue.popleft()
                if lock_state in other_visited:
                    return turns + other_visited[lock_state]
                for next_state in get_next_states(lock_state):
                    if next_state not in deadends and next_state not in visited:    
                        visited[next_state] =  turns + 1
                        queue.append((next_state, turns + 1))
                return 0
        
        while start_queue or end_queue:
            turn_start = bfs(start_queue, start_visited, end_visited)
            if turn_start:
                return turn_start
            turn_end = bfs(end_queue, end_visited, start_visited)
            if turn_end:
                return turn_end
        
        return -1
        