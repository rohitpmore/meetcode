"""
Problem: Word Search
Difficulty: Medium
Time Limit: 30 min

Given an m x n grid of characters, board, and a string word, return TRUE if
word exists in the grid.

The word can be formed by connecting letters of sequentially adjacent cells.
The cells are considered sequentially adjacent when neighbors are either
horizontally or vertically neighbors. Each cell can be used only once while
forming the word.

Constraints:
- m == board.length
- n == board[i].length, where 0 <= i < m
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consist of only lowercase and uppercase English letters

Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: True

Example 2:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "SEE"
Output: True

Example 3:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCB"
Output: False
Explanation: Cannot reuse the 'B' cell
"""

"""
grid

a b - d
q s - - u
w x y z

word = cat

i = 0
j = 2

rec(0,2,at)
    rec(1,2,t)
        rec(1,3,'')

"""
def solution(grid: list[list[str]], word: str) -> bool:

    # time = O(m * n * 4^L)  where l is length of word
    # space = O(1)
    def rec(grid,i, j,  word) -> bool:
        if len(word) == 0 :
            return True
        
        found = False 

        directions = [(0,-1),(0,1),(-1,0),(1,0)]     
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[i]):
                if grid[ni][nj] == word[0]:
                    tmp = grid[ni][nj]
                    grid[ni][nj] = '-'
                    found = rec(grid, ni, nj, word[1:])
                    grid[ni][nj] = tmp
                    if found:
                        return True
        
        return False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if word[0] == grid[i][j]:
                tmp = grid[i][j]
                grid[i][j] = '-'
                found = rec(grid,i, j, word[1:])
                grid[i][j] = tmp
                if found:
                    return True
    
    return False




TEST_CASES = [
    # (input_args, expected_output)
    (([["A","B","C","E"],
       ["S","F","C","S"],
       ["A","D","E","E"]], "ABCCED"), True),

    (([["A","B","C","E"],
       ["S","F","C","S"],
       ["A","D","E","E"]], "SEE"), True),

    (([["A","B","C","E"],
       ["S","F","C","S"],
       ["A","D","E","E"]], "ABCB"), False),

    # Single cell board
    (([["A"]], "A"), True),
    (([["A"]], "B"), False),

    # Word longer than possible path
    (([["A","B"],
       ["C","D"]], "ABCDA"), False),

    # Snake pattern
    (([["A","B","C"],
       ["D","E","F"],
       ["G","H","I"]], "ABCFEDGH"), True),

    # Case sensitivity
    (([["a","b"],
       ["c","d"]], "abdc"), True),
]
