class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        word_to_patterns = defaultdict(list)
        pattern_to_words = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)
                word_to_patterns[word].append(pattern)
        
        visited_from_start = { beginWord : 1 }
        visited_from_end = { endWord : 1 }
        
        start_queue = deque([(beginWord, 1)])
        end_queue = deque([(endWord, 1)])
        
        def bfs(queue, visited, other_visited):
            for _ in range(len(queue)):
                word, length = queue.popleft()
                if word in other_visited:
                    return length + other_visited[word] - 1
                for pattern in word_to_patterns[word]:
                    for neighbor in pattern_to_words[pattern]:
                        if neighbor not in visited:
                            visited[neighbor] = length + 1
                            queue.append((neighbor, length + 1))
            return 0
        
        ans = None
        while start_queue and end_queue:
            if len(start_queue) < len(end_queue):
                ans = bfs(start_queue, visited_from_start, visited_from_end)
            else:
                ans = bfs(end_queue, visited_from_end, visited_from_start)
            if ans:
                return ans
        return 0