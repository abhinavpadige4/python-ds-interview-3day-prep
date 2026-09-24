"""
LeetCode 209 — Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a contiguous subarray whose sum is >= target.
Return 0 if no such subarray exists.

Example:
    Input:  target = 7, nums = [2,3,1,2,4,3]
    Output: 2   (subarray [4,3])

Approach: Sliding window.
    - Expand `right` to add elements; shrink `left` while the window sum
      is >= target, tracking the minimum window size.

Time:  O(n) — each element enters and leaves the window at most once.
Space: O(1)
"""

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """Return the minimum length of a subarray with sum >= target, else 0."""
    left = 0
    window_sum = 0
    best = float("inf")
    for right, val in enumerate(nums):
        window_sum += val
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return best if best != float("inf") else 0


if __name__ == "__main__":
    cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (1, [1], 1),
        (15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 1),
    ]
    for target, nums, expected in cases:
        got = min_sub_array_len(target, nums)
        assert got == expected, f"FAIL target={target} nums={nums}: got {got}, expected {expected}"
    print("All tests passed.")
