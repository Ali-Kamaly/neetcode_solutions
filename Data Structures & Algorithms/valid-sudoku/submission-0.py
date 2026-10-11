class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.isValidRows(board) and self.isValidCols(board) and self.isValidGroups(board):
            return True
        return False

    def isValidRows(self, board):
        for row in board: 
            seen = set()
            #time complexity O(1) - instant check up 
            for val in row:
                if val.isdigit():
                    if val in seen:
                        return False
                    seen.add(val)

        return True

    def isValidCols(self, board):
        for i in range(9):
            seen = set()
            for row in board:
                val = row[i]
                if val.isdigit():
                    if val in seen:
                        return False
                    seen.add(val)

        return True
            
    def isValidGroups(self, board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()

                for row in range(i,i+3):
                    for col in range(j,j+3):
                        val = board[row][col]
                        if val.isdigit():
                            if val in seen:
                                return False
                            seen.add(val)

        return True

    """
    - no duplicate nums in same row
    - no duplicate nums in same col
    - no duplicate nums in same sub-group
    """    
