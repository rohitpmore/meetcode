"""
Problem: K Closest Points to Origin
Difficulty: Medium
Time Limit: 30 min

Description:
You are given an array of points where each element points[i] = [xi, yi]
represents a point on the X-Y plane, along with an integer k. Your task
is to find and return the k points that are closest to the origin [0, 0].

The distance between two points on the X-Y plane is measured using
Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2)

Note: You can return the result in any order. The answer is guaranteed
to be unique, except for the order in which points appear.

Constraints:
- 1 <= k <= points.length <= 10^3
- -10^4 <= xi, yi <= 10^4

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: Distance of [1,3] from origin = sqrt(10)
             Distance of [-2,2] from origin = sqrt(8)
             Since sqrt(8) < sqrt(10), [-2,2] is closer.

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The two closest points to origin are [3,3] and [-2,4].
"""

""" 
points = [3,4], [1,2], [1,1], [-1,2], [3,-2], [-1,-3]
k = 4

mh = [-10,-1,-3],[-5,1,2],[-2,1,1],[-5,-1,2]

i = 4

o/p = [-1,-3] [1,2] [1,1], [-1,2]
"""
from heapq import heapify, heappop, heappush, heappushpop
def solution(points: list[list[int]], k: int) -> list[list[int]]:
    # time = O(k + (n-k)logk)
    # space = O(k)

    mh = []
    heapify(mh)

    for i in range(k):
        heappush(mh, [-(points[i][0]**2 + points[i][1]**2), points[i][0], points[i][1]])

    for i in range(k, len(points)):
        if -(mh[0][0]) > points[i][0]**2 + points[i][1]**2:
            heappushpop(mh, [-(points[i][0]**2 + points[i][1]**2),points[i][0],points[i][1]])

    return [[xi, yi] for _, xi, yi in mh]
        


# Custom comparison for test cases (order doesn't matter, handles ties)
def compare_results(actual, expected):
    if actual is None or len(actual) != len(expected):
        return False
    # Compare by distances (handles ties where different points have same distance)
    dist = lambda p: p[0]**2 + p[1]**2
    return sorted(dist(p) for p in actual) == sorted(dist(p) for p in expected)


TEST_CASES = [
    (([[1, 3], [-2, 2]], 1), [[-2, 2]]),
    (([[3, 3], [5, -1], [-2, 4]], 2), [[-2, 4], [3, 3]]),
    (([[0, 1], [1, 0]], 2), [[0, 1], [1, 0]]),
    (([[1, 1], [2, 2], [3, 3]], 1), [[1, 1]]),
    (([[2, 0], [0, 1], [1, 1], [0, 0]], 2), [[0, 0], [0, 1]]),
]
