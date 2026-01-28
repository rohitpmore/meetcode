"""
Problem: Kth Smallest Element in a Sorted Matrix
Difficulty: Medium

Find the kth smallest element in an (n × n) matrix, where each row and column
of the matrix is sorted in ascending order.

Although there can be repeating values in the matrix, each element is considered
unique and, therefore, contributes to calculating the kth smallest element.

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -10^3 <= matrix[i][j] <= 10^3
- 1 <= k <= n^2

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in sorted order are:
[1, 5, 9, 10, 11, 12, 13, 13, 15], the 8th element is 13.

Example 2:
Input: matrix = [[1,2],[3,4]], k = 3
Output: 3
Explanation: Elements sorted: [1, 2, 3, 4], the 3rd element is 3.

Example 3:
Input: matrix = [[-5]], k = 1
Output: -5
Explanation: Single element matrix.
"""

""" 
matrix = 
    1 2 3
    4 5 6
    7 8 9

k = 5

mh =  [6,1,2], [7,2,0], [8,2,1]
N = 3
visited = {(0,0), (0,1), (1,0), (1,1), (0,2), (1,2), (2,0), (2,1)}
result = 5
c = 5
elem = 5
i = 1
j = 1

"""
from heapq import heapify, heappop, heappush
def solution(matrix: list[list[int]], k: int) -> int:
    mh = []
    heapify(mh)
    N = len(matrix[0])

    for i in range(N):
        heappush(mh, [matrix[i][0],i,0])

    c = 0
    while c < k and len(mh) > 0:
        elem, i, j = heappop(mh)
        if j + 1 < N:
            heappush(mh, [matrix[i][j+1], i, j+1])
        c += 1

    return elem


    
    


# Test cases: ((matrix, k), expected_output)
TEST_CASES = [
    (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13),
    (([[1, 2], [3, 4]], 3), 3),
    (([[-5]], 1), -5),
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5), 5),
    (([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5), 1),  # All same values
    (([[1, 2], [1, 3]], 2), 1),  # Duplicate values across rows
]
