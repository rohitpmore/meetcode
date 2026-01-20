"""
Problem: Valid Palindrome
Difficulty: Easy
Source: LeetCode #125

Given a string s, return True if it is a palindrome; otherwise, return False.

A phrase is considered a palindrome if it reads the same backward as forward
after converting all uppercase letters to lowercase and removing any characters
that are not letters or numbers. Only alphanumeric characters (letters and digits)
are taken into account.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: True
Explanation: After removing non-alphanumeric characters, s is empty "".
An empty string is a palindrome by definition.

Constraints:
- 1 <= s.length <= 3000
- s consists only of printable ASCII characters
"""


def solution(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -=1

    return True    



TEST_CASES = [
    # Basic palindromes
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),

    # Non-palindromes
    ("race a car", False),
    ("hello", False),

    # Edge cases - empty/whitespace
    (" ", True),
    ("", True),

    # Single character
    ("a", True),

    # Only non-alphanumeric (becomes empty)
    (".,!?", True),

    # Mixed case
    ("Aa", True),
    ("Ab", False),

    # With numbers
    ("A1b2b1a", True),
    ("12321", True),
    ("12345", False),

    # Punctuation heavy
    ("No 'x' in Nixon", True),
    ("Was it a car or a cat I saw?", True),
]
