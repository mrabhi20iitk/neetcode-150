class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking rows
        for i in range(len(board)):
            m = {}
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in m:
                        return False
                    else: m[board[i][j]] = 1

        #checking columns
        for i in range(len(board[0])):
            n = {}
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in n: return False
                    else: n[board[j][i]] = 1

        #checking  3 x 3 blocks
        i , j  = 0,0
        while i < 9:
            j = 0
            while j < 9 :
                a = i 
                d = {}
                while a < i+3 : 
                    b = j
                    while b < j+3:
                        if board[a][b] != ".":
                            if board[a][b] in d:
                                return False
                            else: d[board[a][b]] = 1
                        b+=1
                    a+=1
                j+=3
            i+=3

        return True
        