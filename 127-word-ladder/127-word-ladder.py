class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        patterns = defaultdict(list)
        
        graph = defaultdict(list)
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[word].append(pattern)
                graph[pattern].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for pattern in patterns[word]:
                    for neighbor in graph[pattern]:
                        if neighbor not in visited and neighbor != word:
                            queue.append(neighbor)
                            visited.add(neighbor)
            level += 1
        
        return 0