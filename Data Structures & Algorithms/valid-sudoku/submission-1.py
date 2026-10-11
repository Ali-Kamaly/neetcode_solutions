import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9): 
                val = board[r][c]
                box_id = (r//3, c//3)
                if val.isdigit():
                    if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_id].add(val)

        return True
                
