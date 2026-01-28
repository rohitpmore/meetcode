"""
Problem: Range Sum of Sorted Subarray Sums
Difficulty: Medium

You are given an integer array nums containing n positive integers along with
left and right. Calculate the sum of its elements for every non-empty continuous
subarray of nums. Collect these sums into a new array and sort it in nondecreasing
order. This will result in a new array of size n × (n + 1) / 2.

Your task is to return the sum of the elements in this sorted array from the
index left to right (inclusive with 1-based indexing).

Note: As the result can be large, return the sum modulo 10^9 + 7.

Example 1:
Input: nums = [1, 2, 3, 4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4
             Sorted: [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]
             Sum of indices 1 to 5: 1 + 2 + 3 + 3 + 4 = 13

Example 2:
Input: nums = [1, 2, 3, 4], n = 4, left = 3, right = 4
Output: 6
Explanation: Sorted array: [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]
             Sum of indices 3 to 4: 3 + 3 = 6

Example 3:
Input: nums = [1, 2, 3, 4], n = 4, left = 1, right = 10
Output: 50
Explanation: Sum of all elements: 1+2+3+3+4+5+6+7+9+10 = 50

Constraints:
- n == nums.length
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 100
- 1 <= left <= right <= n × (n + 1) / 2
"""

MOD = 10**9 + 7

def solution(nums: list[int], n: int, left: int, right: int) -> int:
    # time = O(n^2 log n^2) -> O(n^2 log n)
    # space = O(n^2)
    subarray = []

    for i in range(len(nums)): #n
        sum = 0
        for j in range(i, len(nums)): #n
            sum += nums[j]
            subarray.append(sum)
    
    subarray.sort() #n^2 log n^2

    res = 0 

    for i in range(left-1, right): #n^2
        res += subarray[i]

    return res %MOD


TEST_CASES = [
    (([1, 2, 3, 4], 4, 1, 5), 13),
    (([1, 2, 3, 4], 4, 3, 4), 6),
    (([1, 2, 3, 4], 4, 1, 10), 50),
    (([1, 1, 1], 3, 1, 6), 10),
    (([5], 1, 1, 1), 5),
    (([100, 100], 2, 1, 3), 400),
    (([1, 2], 2, 1, 3), 6),
]
