"""
Problem: Group Anagrams
Difficulty: Medium
Source: LeetCode #49 (Meta Top Interview Question)

Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: The groups are anagrams of each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Hints:
- Think about what makes two words anagrams of each other
- How can you efficiently represent a "signature" for each anagram group?
"""

from typing import List


def solution(strs: List[str]) -> List[List[str]]:
    # TODO(human): Implement your solution
    pass


# Note: Order within groups and order of groups doesn't matter
# The test runner will sort for comparison
TEST_CASES = [
    ((["eat", "tea", "tan", "ate", "nat", "bat"],), [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    ((["abc", "bca", "cab", "xyz", "zyx"],), [["abc", "bca", "cab"], ["xyz", "zyx"]]),
]
