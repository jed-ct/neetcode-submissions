class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Check rows
        for i in range(0, len(board)):
            column_set = set()
            for j in range(0, len(board[i])):
                if board[i][j] in column_set and board[i][j] != ".":
                    return False
                column_set.add(board[i][j])

        #Check columns
        for i in range(0, len(board)):
            column_set = set()
            for j in range(0, len(board[i])):
                if board[j][i] in column_set and board[j][i] != ".":
                    return False
                column_set.add(board[j][i])

        square_map:dict[list[int], set[str]] = {}
        
        #Check squares
        for i in range(0, len(board)):
            square_y = int(i / 3)
            for j in range(0, len(board[i])):
                square_x = int(j / 3)

                if tuple([square_x, square_y]) in square_map:
                    if board[i][j] in square_map.get(tuple([square_x, square_y])) and board[i][j] != ".":
                        return False
                    else:
                        square_map[tuple([square_x, square_y])].add(board[i][j])
                else:
                    square_map[tuple([square_x, square_y])] = set(board[i][j])


        return True
