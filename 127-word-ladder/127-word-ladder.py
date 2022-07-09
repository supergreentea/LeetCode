class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # O(m^2)
        def get_patterns(word):
            patterns = []
            for i in range(len(word)): # m operations
                patterns.append(word[:i] + "*" + word[i + 1:]) # O(m) to create string
            return patterns
        
        wordList.append(beginWord)
        
        graph = defaultdict(list)
        
        for word in wordList: # n words
            for pattern in get_patterns(word): # m patterns
                graph[pattern].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1
        
        # 
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                patterns = get_patterns(word)
                for pattern in patterns:
                    for neighbor in graph[pattern]:
                        if neighbor not in visited and neighbor != word:
                            visited.add(neighbor)
                            queue.append(neighbor)
            level += 1
        return 0
                
            