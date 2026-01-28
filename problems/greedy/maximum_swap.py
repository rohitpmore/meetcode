"""
Problem: Maximum Swap
Difficulty: Medium
Time Limit: 30 min

Given an integer num, return the maximum number that can be formed by swapping
at most two digits once.

Constraints:
- 0 <= num <= 10^5

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the digit 2 and the digit 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap needed, already the maximum.

Example 3:
Input: num = 1993
Output: 9913
Explanation: Swap the digit 1 and the digit 9 (at position 2).

Example 4:
Input: num = 98368
Output: 98863
Explanation: Swap the digit 3 and the digit 8.
"""

"""
num = 2736
digits = [7,2,3,6]
last = -1 -1 0 2 -1 -1 3 1 -1 -1
i = 0
d = 7 <- 2

"""
def solution(num: int) -> int:

    # time = O(d)
    # space = O(d) where d is number of digits in num
    N = num
    digits = []
    while num > 0 :
        digits.append(num % 10)
        num = num // 10

    if len(digits) <= 1:
        return N
    
    last = [-1] * 10
    digits.reverse()

    for i, d in enumerate(digits):
        last[d] = i
    
    
    for i in range(len(digits)):
        swapped = False
        for d in range(9, digits[i], -1):
            if last[d] > i: 
                digits[i], digits[last[d]] = digits[last[d]], digits[i]
                swapped = True
                break
        
        if swapped:
            break        

    res = 0 

    for d in digits:
        res = res*10 + d

    return res   

            
            



# Test cases
TEST_CASES = [
    ((2736,), 7236),
    ((9973,), 9973),
    ((1993,), 9913),
    ((98368,), 98863),
    ((1234,), 4231),
    ((10,), 10),
    ((12,), 21),
    ((111,), 111),
    ((0,), 0),
]
