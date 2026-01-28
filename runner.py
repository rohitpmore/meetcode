#!/usr/bin/env python3
"""Test runner for MeetCode problems."""

import sys
import importlib.util
import argparse
from pathlib import Path
import time
import traceback


def load_problem(file_path: str):
    """Load a problem module from file path."""
    spec = importlib.util.spec_from_file_location("problem", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tests(file_path: str, verbose: bool = False):
    """Run test cases for a problem."""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        return False

    try:
        module = load_problem(file_path)
    except Exception as e:
        print(f"Error loading problem: {e}")
        if verbose:
            traceback.print_exc()
        return False

    if not hasattr(module, 'solution'):
        print("Error: No 'solution' function found in problem file")
        return False

    if not hasattr(module, 'TEST_CASES'):
        print("Error: No 'TEST_CASES' found in problem file")
        return False

    # Use solution_wrapper if available (for tree/graph problems), else solution
    if hasattr(module, 'solution_wrapper'):
        solution = module.solution_wrapper
    else:
        solution = module.solution
    test_cases = module.TEST_CASES

    print(f"\n{'='*50}")
    print(f"Running: {path.name}")
    print(f"{'='*50}\n")

    passed = 0
    failed = 0

    for i, (inputs, expected) in enumerate(test_cases, 1):
        # Handle both single and multiple inputs
        if not isinstance(inputs, tuple):
            inputs = (inputs,)

        try:
            start = time.perf_counter()
            result = solution(*inputs)
            elapsed = (time.perf_counter() - start) * 1000

            # Check result (use custom compare if available)
            compare_fn = getattr(module, 'compare_results', lambda a, e: a == e)
            if compare_fn(result, expected):
                passed += 1
                status = "PASS"
                if verbose:
                    print(f"Test {i}: {status} ({elapsed:.2f}ms)")
                    print(f"  Input: {inputs}")
                    print(f"  Output: {result}\n")
            else:
                failed += 1
                status = "FAIL"
                print(f"Test {i}: {status}")
                print(f"  Input:    {inputs}")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}\n")

        except Exception as e:
            failed += 1
            print(f"Test {i}: ERROR")
            print(f"  Input: {inputs}")
            print(f"  Error: {e}")
            if verbose:
                traceback.print_exc()
            print()

    # Summary
    total = passed + failed
    print(f"{'='*50}")
    print(f"Results: {passed}/{total} passed", end="")
    if failed == 0 and total > 0:
        print(" - ALL TESTS PASSED!")
    else:
        print()
    print(f"{'='*50}\n")

    return failed == 0


def main():
    parser = argparse.ArgumentParser(description="Run test cases for a problem")
    parser.add_argument("file", help="Path to problem file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()
    success = run_tests(args.file, args.verbose)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
