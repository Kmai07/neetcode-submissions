class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initialize our 3 tracking systems
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # We will use (r // 3, c // 3) as the key

        # 2. Scan every square on the 9x9 board
        for r in range(9):
            for c in range(9):
                
                # If the square is empty, just skip it
                if board[r][c] == ".":
                    continue
                
                # --- YOUR LOGIC GOES HERE ---
                # 1. Check if board[r][c] is ALREADY inside rows[r], cols[c], or boxes[(r // 3, c // 3)]
                # 2. If it is, the board is invalid. Return False.
                # 3. If it is not, add board[r][c] to all three sets so we track it for the future.
                # ----------------------------
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in boxes[(r//3, c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
                    
                

        # If we check every single square and never find a duplicate, it's valid!
        return True