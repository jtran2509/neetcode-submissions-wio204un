import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                digit = board[r][c]

                # Check whether this number existed already
                if (digit in rows[r] or
                    digit in cols[c] or
                    digit in squares[(r // 3, c //3)]):
                    return False

                # If not, then add the number to the according boxes
                rows[r].add(digit)
                cols[c].add(digit)
                squares[(r//3, c//3)].add(digit)
        return True