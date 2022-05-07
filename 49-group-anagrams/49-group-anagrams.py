class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            key = ""
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            Dict[tuple(charCount)].append(s)
        return Dict.values()