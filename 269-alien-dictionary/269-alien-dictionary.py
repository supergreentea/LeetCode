class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        G = {}
        indegree = defaultdict(int)
        
        if len(words) == 1:
            return ''.join(list(set([c for c in words[0]])))
        
        # create adjacency list of leters 
        for i in range(len(words) - 1):
            cur_word = words[i]
            next_word = words[i + 1]
            
            # create adjacency list for all letters so we can check if topological ordering has all letters later
            for c in cur_word:
                if c not in G:
                    G[c] =  []
            for c in next_word:
                if c not in G:
                    G[c] = []
            
            min_length = min(len(cur_word), len(next_word))
            diff_found = False
            for i in range(min_length):
                if cur_word[i] != next_word[i]:
                    G[cur_word[i]].append(next_word[i])
                    indegree[next_word[i]] += 1
                    diff_found = True
                    break # the comparisons past the first difference are not meaningful
            if not diff_found and len(cur_word) > len(next_word):
                return ""
            
        zero_indegree = [letter for letter in G if indegree[letter] == 0]
        top_ordering = []
        
        while zero_indegree:
            letter = zero_indegree.pop()
            top_ordering.append(letter)
            for neighbor in G[letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree.append(neighbor)
        
        return ''.join(top_ordering) if len(top_ordering) == len(G) else ""
        
        
        
        