class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # assuming board is always 9x9
        for i in range(9):
            row_integers = [k for k in board[i] if k != '.']  # get row integers
            if len(row_integers) > len(set(row_integers)):  # check for repeats
                return False
            col_integers = [k[i] for k in board if k[i] != '.']  # get col integers
            if len(col_integers) > len(set(col_integers)):  # check for repeats
                return False

        for i in [0, 3, 6]:  # get subsquares
            for j in [0, 3, 6]:
                segment_integers = [elem for chunk in board[j:(j+3)] for elem in chunk[i:(i+3)] if elem != '.']
                if len(segment_integers) > len(set(segment_integers)):  # check for repeats
                    return False
        return True
