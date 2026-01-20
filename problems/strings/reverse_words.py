"""
Problem: Reverse Words in a String
Difficulty: Medium
Source: LeetCode #151

You are given a string sentence that may contain leading or trailing spaces,
as well as multiple spaces between words. Your task is to reverse the order
of the words in the sentence without changing the order of characters within
each word.

Return the resulting modified sentence as a single string with words separated
by a single space, and no leading or trailing spaces.

Note: A word is defined as a continuous sequence of non-space characters.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world  "
Output: "world hello"
Explanation: Reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: Multiple spaces between words reduced to single space.

Constraints:
- 1 <= sentence.length <= 10^4
- sentence contains English uppercase and lowercase letters, digits, and spaces
- There is at least one word in the sentence
"""


def solution(sentence: str) -> str:
    # TODO(human): Implement two-pointer approach
    # Steps: 1) Convert to list  2) Reverse entire list  3) Reverse each word  4) Handle spaces
    # Hint: Write a helper function reverse(chars, left, right) to reverse a portion in-place

    # Your built-in solution (keep for reference):
    words = sentence.split()
    return ' '.join(words[::-1])



TEST_CASES = [
    # Basic cases from examples
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),

    # Single word
    ("hello", "hello"),
    ("  hello  ", "hello"),

    # Two words
    ("hello world", "world hello"),
    ("  hello   world  ", "world hello"),

    # Multiple spaces everywhere
    ("   spaces   everywhere   here   ", "here everywhere spaces"),

    # Mixed content (letters, digits)
    ("test123 abc456", "abc456 test123"),
    ("  code 2 win  ", "win 2 code"),

    # Longer sentence
    ("the quick brown fox jumps over the lazy dog", "dog lazy the over jumps fox brown quick the"),

    # Single character words
    ("a b c d e", "e d c b a"),

    # Leading/trailing with single word
    ("   word   ", "word"),
]
