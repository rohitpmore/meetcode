"""
Problem: Spiral Matrix
Difficulty: Medium

Given an m × n matrix, return an array containing the matrix elements in spiral
order, starting from the top-left cell.

The spiral order traverses:
1. Left to right across the top row
2. Top to bottom down the right column
3. Right to left across the bottom row
4. Bottom to top up the left column
5. Repeat inward until all elements are visited

Example 1:
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Explanation:
  → → →
  ↑   ↓
  ← ← ↓
  Spiral: 1→2→3→6→9→8→7→4→5

Example 2:
Input: matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Example 3:
Input: matrix = [[1]]
Output: [1]

Example 4:
Input: matrix = [[1, 2],
                 [3, 4]]
Output: [1, 2, 4, 3]

Constraints:
- 1 <= matrix.length <= 10
- 1 <= matrix[i].length <= 10
- -100 <= matrix[i][j] <= 100
"""

"""
matrix

1   2   3   4
5   6   7   8
9   10  11  12

M = 2
N = 3
m = 1
n = 1

i = 1
j = 1
res = [1 2 3 4 8 12 11 10 9 5 6 7]
"""

def solution(matrix: list[list[int]]) -> list[int]:
    """
    Return elements of matrix in spiral order.
    """
    M = len(matrix)
    N = len(matrix[0])

    m = 0
    n = 0
    res = []

    while m < M and n < N:
        # go right
        i = m
        j = n
        while j < N:
            res.append(matrix[i][j])
            j += 1
        
        # go down
        i = m + 1
        j = N - 1
        while i < M:
            res.append(matrix[i][j])
            i += 1
        
        # go left
        i = M - 1
        j = N - 2
        if m != M - 1:
            while j >= n:
                res.append(matrix[i][j])
                j -= 1
        
        # go up
        i = M - 2
        j = n
        if n != N - 1:
            while i > m:
                res.append(matrix[i][j])
                i -= 1
        m += 1
        n += 1
        M -= 1
        N -= 1
        
    return res



TEST_CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    (([[1]],), [1]),
    (([[1, 2], [3, 4]],), [1, 2, 4, 3]),
    (([[1, 2, 3]],), [1, 2, 3]),  # Single row
    (([[1], [2], [3]],), [1, 2, 3]),  # Single column
    (([[1, 2, 3, 4, 5]],), [1, 2, 3, 4, 5]),  # Wide single row
    (([[1], [2], [3], [4], [5]],), [1, 2, 3, 4, 5]),  # Tall single column
    (([[1, 2], [3, 4], [5, 6]],), [1, 2, 4, 6, 5, 3]),  # 3x2 matrix
]
