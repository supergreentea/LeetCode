class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns_to_words = defaultdict(list)
        words_to_patterns = defaultdict(list)
        
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0 : i] + "*" + word[i+1:]
                words_to_patterns[word].append(pattern)
                patterns_to_words[pattern].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for pattern in words_to_patterns[word]:
                    for neighbor in patterns_to_words[pattern]:
                        if neighbor not in visited and neighbor != word:
                            visited.add(neighbor)
                            queue.append(neighbor)
            level += 1
        
        return 0
        