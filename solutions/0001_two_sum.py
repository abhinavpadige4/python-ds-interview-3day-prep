"""
LeetCode 1 — Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return indices
of the two numbers such that they add up to `target`. Each input has
exactly one solution and you may not use the same element twice.

Example:
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]

Approach: Hash map.
    - For each num, check if (target - num) is already in the map.
    - If yes, return the stored index and current index.
    - Otherwise, store num -> index.

Time:  O(n)
Space: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers in `nums` that sum to `target`."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # unreachable given problem constraints


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
    for nums, target, expected in cases:
        got = two_sum(nums, target)
        assert got == expected, f"FAIL {nums} target={target}: got {got}, expected {expected}"
    print("All tests passed.")
