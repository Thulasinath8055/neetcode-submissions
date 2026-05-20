class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        # Write code for 1st constraint
        for i in range(9):
            row = board[i]
            seen = set()
            for j in range(9):
                if row[j] == ".":
                    continue
                if row[j] in seen:
                    flag = False
                    return flag
                else:
                    seen.add(row[j])
        
        # Write code for second constraint
        for col_index in range(9):
            column = [row[col_index] for row in board]
            seen = set()
            for j in range(9):
                if column [j] == ".":
                    continue
                if column[j] in seen:
                    flag = False
                    return flag
                else:
                    seen.add(column[j])
        
        # write code for last constraint
        # we need to access the 3*3 blocks of total 9
        for r in range(0,9,3):
            for c in range(0,9,3):
                block = []
                
                for i in range(3):
                    for j in range(3):
                        block.append(board[r+i][c+j])
                seen = set()
                for val in block:
                    if val == ".":
                        continue
                    if val in seen:
                        flag = False
                        return flag
                    else:
                        seen.add(val)  
        return flag    