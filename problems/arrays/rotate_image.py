"""
Problem: Rotate Image
Difficulty: Medium

Given an n × n matrix, rotate the matrix 90 degrees clockwise.
The rotation must be done IN PLACE - modify the matrix directly
without allocating another matrix.

Example 1:
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

Visualization:
  1 2 3      7 4 1
  4 5 6  →   8 5 2
  7 8 9      9 6 3

Example 2:
Input: matrix = [[1, 2],
                 [3, 4]]
Output: [[3, 1],
         [4, 2]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[5,  1,  9,  11],
                 [2,  4,  8,  10],
                 [13, 3,  6,  7],
                 [15, 14, 12, 16]]
Output: [[15, 13, 2,  5],
         [14, 3,  4,  1],
         [12, 6,  8,  9],
         [16, 7,  10, 11]]

Constraints:
- matrix.length == matrix[i].length (square matrix)
- 1 <= matrix.length <= 20
- -1000 <= matrix[i][j] <= 1000
"""

"""
matrix
7   4   1
8   5   2
9   6   3

i = 1
j1 = 0
j2 = 2
"""
def solution(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate matrix 90 degrees clockwise in-place.
    Return the modified matrix.
    """
    # time = O(n^2)
    # space = O(1)
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

    for i in range(len(matrix)):
        j1,j2 = 0, len(matrix)-1
        while j1 < j2:
            matrix[i][j2], matrix[i][j1] = matrix[i][j1], matrix[i][j2]
            j1 += 1
            j2 -= 1
    
    return matrix


# Helper to deep copy matrix for testing (since we modify in place)
def solution_wrapper(matrix):
    import copy
    mat_copy = copy.deepcopy(matrix)
    result = solution(mat_copy)
    return result if result is not None else mat_copy


TEST_CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    (([[1, 2], [3, 4]],), [[3, 1], [4, 2]]),
    (([[1]],), [[1]]),
    (([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],),
     [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]),
]
