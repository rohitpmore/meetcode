"""
Problem: Permutations
Difficulty: Medium
Time Limit: 30 min

Given an input string, word, return all possible permutations of the string.

Note: The order of permutations does not matter.

Constraints:
- All characters in word are unique.
- 1 <= word.length <= 6
- All characters in word are lowercase English letters.

Example 1:
Input: word = "ab"
Output: ["ab", "ba"]

Example 2:
Input: word = "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

Example 3:
Input: word = "a"
Output: ["a"]
"""

"""
word = abc

rec([a,b,c], 0)
    j = 0
        rec([a,b,c], 1)
            j = 1
                rec([a,b,c], 2)
                    "abc"
            j = 2
                rec([a,c,b], 2)
                    "acb"
    j = 1
        rec([b,a,c], 1)
            j = 1
                rec([b,a,c], 2)
                    "bac"
            j = 2
                rec([b,c,a], 2)
                    "bca"
    j = 2
        rec([c,b,a], 1)
            j = 1
                rec([c,b,a], 2)
                    "cba"
            j = 2
                rec([c,a,b], 2)
                    "cab"
"""

def solution(word: str) -> list[str]:
    # time -> O(n! x n)
    # space -> O(n)
    result = []

    def rec(chars, index):
        if index == len(chars) -1:
            result.append(''.join(chars))
        else:
            for j in range(index, len(chars)):
                chars[index], chars[j] = chars[j], chars[index]
                rec(chars, index +1)
                chars[index], chars[j] = chars[j], chars[index] #undo -> backtracking


    rec(list(word), 0)
    return result






# Test cases - order doesn't matter, so we compare as sets
TEST_CASES = [
    (("ab",), {"ab", "ba"}),
    (("abc",), {"abc", "acb", "bac", "bca", "cab", "cba"}),
    (("a",), {"a"}),
    (("bad",), {"bad", "bda", "abd", "adb", "dba", "dab"}),
]


def compare_results(result, expected):
    """Custom comparator since order doesn't matter"""
    if result is None:
        return False
    return set(result) == expected
