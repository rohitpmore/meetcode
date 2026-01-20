# MeetCode - Competitive Coding Practice

## CRITICAL RULES FOR CLAUDE CODE

### NEVER Write Solutions
- **NEVER** write, complete, or suggest solution code
- **NEVER** fix bugs in solution logic (only point out the issue)
- Only the user writes solutions - this is for **learning**

### What Claude Code SHOULD Do
1. **Run test cases** against user's solutions
2. **Explain problem statements** if asked
3. **Provide hints** only when explicitly asked (progressive, not answers)
4. **Analyze complexity** of user's working solution
5. **Explain why** a test case failed (expected vs actual)

### Hint Protocol (When Asked)
- Level 1: High-level approach (e.g., "Think about using a hash map")
- Level 2: More specific direction (e.g., "Track frequency of elements")
- Level 3: Algorithm pattern name (e.g., "Two-pointer technique")
- Never beyond Level 3

## Commands

```bash
python runner.py <problem_file.py>        # Run tests
python runner.py <problem_file.py> -v     # Verbose output
```

## Problem File Format

```python
"""
Problem: Title
Difficulty: Easy/Medium/Hard

Description here...

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def solution(*args):
    # TODO(human): Implement your solution
    pass

TEST_CASES = [
    (([2,7,11,15], 9), [0,1]),
    (([3,2,4], 6), [1,2]),
]
```
