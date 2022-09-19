class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            s = path.split(' ')
            directory = s[0]
            files = s[1:]
            for file in files:
                open_index, close_index = file.find("("), file.find(")")
                content = file[open_index + 1 : close_index]
                content_to_paths[content].append(directory + "/" + file[:open_index])
        return [val for val in content_to_paths.values() if len(val) >= 2]