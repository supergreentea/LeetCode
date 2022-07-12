class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False
        
        start_pieces, target_pieces = [], []

        for index, char in enumerate(start):
            if char != '_':
                start_pieces.append((char, index))
        for index, char in enumerate(target):
            if char != '_':
                target_pieces.append((char, index))
        
        if len(start_pieces) != len(target_pieces):
            return False
        
        for i in range(len(start_pieces)):
            start_char, start_index = start_pieces[i]
            target_char, target_index = target_pieces[i]
            if start_char == target_char:
                if start_char == 'L':
                    if start_index < target_index:
                        return False
                else:
                    if start_index > target_index:
                        return False
            else:
                return False
        
        return True
        