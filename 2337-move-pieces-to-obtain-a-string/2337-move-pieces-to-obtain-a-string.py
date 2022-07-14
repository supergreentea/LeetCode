class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_pieces, target_pieces = [], []
        
        if len(start) != len(target):
            return False
        
        for i in range(len(start)):
            if start[i] != '_':
                start_pieces.append((start[i], i))
            if target[i] != '_':
                target_pieces.append((target[i], i))
        
        if len(start_pieces) != len(target_pieces):
            return False
        
        for i in range(len(start_pieces)):
            start_piece, start_piece_index = start_pieces[i]
            target_piece, target_piece_index = target_pieces[i]
            if start_piece != target_piece:
                return False
            else:
                if start_piece == 'L':
                    if start_piece_index < target_piece_index:
                        return False
                else:
                    if start_piece_index > target_piece_index:
                        return False
        
        return True