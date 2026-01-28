"""
Problem: Set Matrix Zeros
Difficulty: Medium

Given an m x n matrix, if any element is zero, set its entire row and column
to zeros. You must do this IN PLACE - modify the matrix directly without
allocating another matrix.

Example 1:
Input: mat = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
Output: [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]
Explanation: mat[1][1] is 0, so row 1 and column 1 are set to 0.

Example 2:
Input: mat = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
Output: [[0, 0, 0, 0],
         [0, 4, 5, 0],
         [0, 3, 1, 0]]
Explanation: mat[0][0] and mat[0][3] are 0, so rows/cols are zeroed accordingly.

Example 3:
Input: mat = [[1, 2, 3],
              [4, 5, 6]]
Output: [[1, 2, 3],
         [4, 5, 6]]
Explanation: No zeros in matrix, so nothing changes.

Constraints:
- 1 <= m, n <= 20
- -2^31 <= mat[i][j] <= 2^31 - 1

Follow-up: Can you solve it with O(1) extra space? (not counting the input matrix)
"""

def solution(mat: list[list[int]]) -> None:
    """
    Modify mat in-place to set rows and columns to zero.
    """
    first_col_has_zeros, first_row_has_zeros = False, False
    for i in range(len(mat)):
        if mat[i][0] == 0:
            first_col_has_zeros = True
    for j in range(len(mat[0])):
        if mat[0][j] == 0:
            first_row_has_zeros = True

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0


    if first_col_has_zeros:
        for i in range(len(mat)):
            mat[i][0] = 0
    
    if first_row_has_zeros:
        for j in range(len(mat[0])):
            mat[0][j] = 0


# Helper to deep copy matrix for testing (since we modify in place)
def solution_wrapper(mat):
    import copy
    mat_copy = copy.deepcopy(mat)
    solution(mat_copy)
    return mat_copy


TEST_CASES = [
    (([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    (([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    (([[1, 2, 3], [4, 5, 6]],), [[1, 2, 3], [4, 5, 6]]),
    (([[0]],), [[0]]),
    (([[1]],), [[1]]),
    (([[1, 0], [0, 1]],), [[0, 0], [0, 0]]),
    (([[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],),
     [[1, 0, 3, 0], [0, 0, 0, 0], [9, 0, 11, 0], [0, 0, 0, 0]]),
]
