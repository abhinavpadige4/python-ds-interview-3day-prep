"""
LeetCode 283 — Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements. Must be done in-place without
copying another array.

Example:
    Input:  nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Approach: Two-pointer.
    - `write` tracks the next index where a non-zero should be placed.
    - Iterate `read` across the array; when nums[read] != 0, swap it with
      nums[write] and advance write.
    - After the loop, all non-zeros are packed at the front in original
      order, and everything from `write` onward is already 0.

Time:  O(n) — single pass.
Space: O(1) — in-place.
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """Move all zeros to the end of `nums` in-place."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# ---------- Self-test ----------
if __name__ == "__main__":
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
    ]
    for nums, expected in cases:
        arr = nums.copy()
        move_zeroes(arr)
        assert arr == expected, f"FAIL {nums}: got {arr}, expected {expected}"
    print("All tests passed.")
