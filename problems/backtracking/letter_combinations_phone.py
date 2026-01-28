"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium
Time Limit: 30 min

Description:
Given a string containing digits from 2 to 9 inclusive, return all possible
letter combinations that the number could represent. Return the answer in any order.

The mapping of digits to letters (like on a telephone dial pad) is:
    2 -> "abc"
    3 -> "def"
    4 -> "ghi"
    5 -> "jkl"
    6 -> "mno"
    7 -> "pqrs"
    8 -> "tuv"
    9 -> "wxyz"

Note: The number 1 does not map to any letters.

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

Examples:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "79"
Output: ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]
"""

from typing import List

"""
digits = "23"

d = 3
result = ['a','b','c']
result = ['ad','bd','cd','ae','be','ce','af','bf','cf']

"""

def solution(digits: str) -> List[str]:
    # time = O(n**2)
    # space = O(n**2) 
    digitsToChar = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r', 's'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
    }


    if len(digits) == 0:
        return []

    result = [""]

    for d in digits:
        nr = []
        for r in result:
            for c in digitsToChar[d]:
                nr.append(r+c)
        
        result = nr

    return result
    

TEST_CASES = [
    # (input_args, expected_output)
    (("23",), ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    (("",), []),
    (("2",), ["a","b","c"]),
    (("79",), ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]),
    (("234",), ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]),
    (("7",), ["p","q","r","s"]),
    (("9",), ["w","x","y","z"]),
    (("22",), ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]),
]
