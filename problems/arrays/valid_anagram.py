"""
Problem: Valid Anagram
Difficulty: Easy
Source: LeetCode #242 (Meta Interview Question)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Follow-up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?
"""


def solution(s: str, t: str) -> bool:
    # TODO(human): Implement your solution
    pass


TEST_CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("a", "a"), True),
    (("a", "b"), False),
    (("ab", "a"), False),
    (("listen", "silent"), True),
    (("hello", "world"), False),
]
