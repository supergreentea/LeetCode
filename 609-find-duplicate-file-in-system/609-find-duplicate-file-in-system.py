class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            s = path.split(' ')
            directory = s[0]
            files = s[1:]
            for file in files:
                open_index = file.find("(")
                content = file[open_index + 1 : file.find(")")]
                content_to_paths[content].append(directory + "/" + file[:open_index])
        res = []
        for key, value in content_to_paths.items():
            if len(value) >= 2:
                res.append(value)
        return res