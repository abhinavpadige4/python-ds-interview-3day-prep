"""
LeetCode 977 — Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a_sorted_array/

Given an integer array `nums` sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Example:
    Input:  nums = [-4,-1,-1,0,1,3]
    Output: [0,1,1,1,9,16]

Approach: Two-pointer from both ends.
    - The largest square is at either the leftmost (most negative) or
      rightmost (largest positive) element.
    - Fill the result from the back, always picking the larger square.

Time:  O(n)
Space: O(n) for the output array.
"""

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """Return squares of `nums` sorted in non-decreasing order."""
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    idx = n - 1
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result[idx] = left_sq
            left += 1
        else:
            result[idx] = right_sq
            right -= 1
        idx -= 1
    return result


if __name__ == "__main__":
    cases = [
        ([-4, -1, -1, 0, 1, 3], [0, 1, 1, 1, 9, 16]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([], []),
        ([0], [0]),
        ([1, 2, 3], [1, 4, 9]),
    ]
    for nums, expected in cases:
        got = sorted_squares(nums)
        assert got == expected, f"FAIL {nums}: got {got}, expected {expected}"
    print("All tests passed.")
