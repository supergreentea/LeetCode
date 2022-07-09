class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        
        def get_key(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        
        for word in strs:
            key = get_key(word)
            groupings[key].append(word)
        
        return groupings.values()