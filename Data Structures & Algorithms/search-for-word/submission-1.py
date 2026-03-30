class Solution:
    def backtrack(self, board, x, y, word, j, seen):
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        if j == len(word):
            return True
        
        for d in directions:
            x_new = x + d[0]
            y_new = y + d[1]
            
            if (x_new, y_new) in seen or x_new < 0 or y_new < 0 or x_new >= len(board) or y_new >= len(board[0]):
                continue
            
            if board[x_new][y_new] == word[j]:
                seen.add((x_new, y_new))
                val = self.backtrack(board, x_new, y_new, word, j + 1, seen)
                if val:
                    return True
                seen.remove((x_new,y_new))
        
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        # indexes on board, word, index of word
        rows = len(board)
        cols = len(board[0])
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:  # add this check
                    seen.add((row, col))        # add starting cell
                    if self.backtrack(board, row, col, word, 1, seen):  # j=1, not 0
                        return True
                    seen.remove((row, col))
        
        return False
            
