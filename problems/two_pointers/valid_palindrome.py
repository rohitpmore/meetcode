"""
Problem: Valid Palindrome
Difficulty: Easy
Source: LeetCode #125 (Meta Interview Question)

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Hints:
- Use two pointers from both ends
- Skip non-alphanumeric characters
"""


def solution(s: str) -> bool:
    # TODO(human): Implement your solution
    pass


TEST_CASES = [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    ((" ",), True),
    (("a",), True),
    (("ab",), False),
    (("aba",), True),
    (("0P",), False),
]
