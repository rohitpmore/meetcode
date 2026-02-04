# MeetCode - Competitive Coding Practice

## Project Structure

Problems are organized by category in `problems/` directory:
```
problems/
├── arrays/          # Array manipulation, intervals, etc.
├── strings/         # String problems
├── two_pointers/    # Two-pointer technique problems
├── sliding_window/  # Sliding window problems
├── linked_lists/    # Linked list problems
├── heap/            # Heap/Priority queue problems
└── [new_category]/  # Add as needed
```

When creating a new problem file:
1. Identify the primary technique/data structure
2. Place in appropriate category folder
3. Use snake_case for filename (e.g., `k_pairs_smallest_sums.py`)

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

## Testing Protocol

When asked to test a solution:
1. **First check for syntax errors** using `python -m py_compile <file>`
2. **If syntax is valid**, proceed to run tests
3. **Always activate venv first**: `source venv/bin/activate`

## Commands

```bash
source venv/bin/activate                  # Always activate first
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

## Problems to Revisit (Needed Hints)

Track problems where hints were requested. Revisit these later for reinforcement.

| Problem | Category | Hint Level | Date |
|---------|----------|------------|------|
| Decode String | strings | Level 3 | 2026-02-02 |
| Exclusive Time of Functions | stacks | Level 3 | 2026-02-02 |
| Graph Valid Tree | graphs | Level 2 | 2026-02-04 |
| Tree Diameter | graphs | Level 3 | 2026-02-04 |
| Tree Diameter (DFS) | graphs | Level 3 | 2026-02-04 |
