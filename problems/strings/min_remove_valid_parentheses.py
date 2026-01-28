"""
Problem: Minimum Remove to Make Valid Parentheses
Difficulty: Medium

Given a string s that may have matched and unmatched parentheses, remove the
minimum number of parentheses so that the resulting string represents a valid
parenthesization.

A valid parenthesization means:
- Every opening parenthesis '(' has a corresponding closing ')'
- Every closing parenthesis ')' has a corresponding opening '('
- Parentheses are properly nested

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: Remove the last ')' which has no matching '('.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Explanation: Remove the first ')' which has no matching '('.

Example 3:
Input: s = "))(("
Output: ""
Explanation: All parentheses are unmatched, remove all of them.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)" or "(ab(c)d)" or "(a(bc)d)"
Explanation: Remove one '(' - multiple valid answers possible.

Example 5:
Input: s = "a(b)c"
Output: "a(b)c"
Explanation: Already valid, no removal needed.

Constraints:
- 1 <= s.length <= 10^3
- s[i] is '(', ')', or a lowercase English letter
"""

"""
s = (a(b(c)d)

st = 
ind = (0)
ns = a(b(c)d)
"""
from collections import deque
def solution(s: str) -> str:
    """
    Remove minimum parentheses to make the string valid.
    Return the resulting valid string.
    """

    # time = O(n)
    # space = O(n)

    st = deque()
    ind = set()

    for i, c in enumerate(s): #n
        if c == '(':
            st.append(i)
        elif c == ')':
            if not st: #empty
                ind.add(i)
            else:
                st.pop()
        else:
            continue

    while len(st) > 0: #n
        i = st.pop()
        ind.add(i)
    
    ns = []

    for i, c in enumerate(s): #n
        if i not in ind:
            ns.append(c)
    
    return ''.join(ns)
    



# Custom compare function - multiple valid answers possible
def compare_results(result, expected):
    """Check if result is a valid parenthesization with same non-paren chars."""
    if result is None:
        return False

    # Check valid parenthesization
    balance = 0
    for c in result:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance < 0:
                return False
    if balance != 0:
        return False

    # Check same letters in same order
    result_letters = [c for c in result if c not in '()']
    expected_letters = [c for c in expected if c not in '()']
    if result_letters != expected_letters:
        return False

    # Check same number of valid parens (minimum removal)
    result_parens = sum(1 for c in result if c in '()')
    expected_parens = sum(1 for c in expected if c in '()')
    return result_parens == expected_parens


TEST_CASES = [
    (("lee(t(c)o)de)",), "lee(t(c)o)de"),
    (("a)b(c)d",), "ab(c)d"),
    (("))((",), ""),
    (("(a(b(c)d)",), "a(b(c)d)"),
    (("a(b)c",), "a(b)c"),
    (("",), ""),  # Edge case: empty string
    (("abc",), "abc"),  # No parentheses
    (("()",), "()"),  # Single valid pair
    (("(((",), ""),  # All opening
    ((")))",), ""),  # All closing
    (("(a)(b)(c)",), "(a)(b)(c)"),  # Multiple valid pairs
    (("((a))",), "((a))"),  # Nested valid
]
