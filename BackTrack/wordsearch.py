from typing import List, Set, Tuple

#O(row * col * (4 ^ n))
def exist(board: List[List[str]], word: str) -> bool:
    
    #O(4 ^ n) where n is the len of word
    def dfs(row: int, col: int, idx: int) -> bool:

        if board[row][col] != word[idx]:
            return False

        visited.add((row,col))

        if idx == len(word) - 1:
            return True

        dirs: List[Tuple[int,int]] = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        for r,c in dirs:
            if not(0 <= r and r < len(board) and 0 <= c and c < len(board[0])):
                continue

            if (r,c) in visited:
                continue
            
            if dfs(r,c, idx + 1):
                return True

        visited.remove((row,col))

        return False 
    
    visited: Set[Tuple[int,int]] = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i,j,0):
                return True

    return False



board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
output = True
print(exist(board, word) == output)


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
output = True
print(exist(board, word) == output)


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
output = False
print(exist(board, word) == output)


board = [["a","b"],
         ["c","d"]]
word = "cdba"
output = True
print(exist(board,word) == output)


board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]

word = "ABCESEEEFS" 
output = True
print(exist(board,word) == output)


# neetcode style solution
class Solution:
    # O(n * m * 4^n)
    def exist(self, board: List[List[str]], word: str) -> bool:        
        ROW: int = len(board)
        COL: int = len(board[0])
        path: Set[Tuple[int,int]] = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True

            if (
                not(0 <= r and r < ROW)
                or not(0 <= c and c < COL)
                or board[r][c] != word[i]
                or (r,c) in path
                ):
                return False
            
            path.add((r,c))
            res = (
                   dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r,c))
            return res
        
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        # count = defaultdict(int, sum(map(Counter, board), Counter()))
        # if count[word[0]] > count[word[-1]]:
        #    word = word[::-1]

        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False

