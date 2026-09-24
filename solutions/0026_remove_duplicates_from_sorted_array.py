"""
LeetCode 26 — Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array `nums` sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
Return the length of the unique portion.

Example:
    Input:  nums = [1,1,2]
    Output: 2, nums[:2] == [1,2]

Approach: Two-pointer.
    - `write` points to the next slot for a unique value.
    - Compare nums[read] with nums[write-1]; if different, write it.

Time:  O(n)
Space: O(1)
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """Return the length of the unique prefix of `nums` after in-place dedup."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5], 5),
    ]
    for nums, expected_len in cases:
        arr = nums.copy()
        length = remove_duplicates(arr)
        assert length == expected_len, f"FAIL {nums}: got {length}, expected {expected_len}"
    print("All tests passed.")
