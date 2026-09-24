"""
LeetCode 27 — Remove Element
https://leetcode.com/problems/remove-element/

Given an array `nums` and a value `val`, remove all occurrences of `val`
in-place. Return the new length. The order of remaining elements doesn't
matter.

Example:
    Input:  nums = [3,2,2,3], val = 3
    Output: 2, nums[:2] == [2,2]

Approach: Two-pointer (compact non-matching values to the front).

Time:  O(n)
Space: O(1)
"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """Remove all occurrences of `val` from `nums` in-place; return new length."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    cases = [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2, 3, 0, 0, 2], 2, 6),
        ([], 1, 0),
        ([1, 1, 1], 1, 0),
        ([1, 2, 3], 4, 3),
    ]
    for nums, val, expected_len in cases:
        arr = nums.copy()
        length = remove_element(arr, val)
        assert length == expected_len, f"FAIL {nums} val={val}: got {length}, expected {expected_len}"
    print("All tests passed.")
