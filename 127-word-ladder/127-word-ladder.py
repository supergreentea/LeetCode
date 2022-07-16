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
        print(word_to_patterns)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for pattern in word_to_patterns[word]:
                    for word in pattern_to_words[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
        return 0