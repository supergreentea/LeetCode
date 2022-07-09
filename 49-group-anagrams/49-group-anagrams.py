class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        
        def get_key(word):
            count = [0] * 26
            for c in word: # O(len(word)) or O(K) where K is max length of string
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        
        for word in strs: # O(n)
            key = get_key(word)
            groupings[key].append(word)
        
        return groupings.values()