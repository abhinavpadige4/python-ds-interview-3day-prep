"""
LeetCode 349 — Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and the result
may be returned in any order.

Example:
    Input:  nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Approach: Hash set.
    - Convert nums1 to a set for O(1) membership.
    - Iterate nums2, add to result set only if the value is in nums1_set.

Time:  O(m + n)
Space: O(m + n)
"""

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return the unique intersection of nums1 and nums2."""
    s1 = set(nums1)
    s2 = set(nums2)
    return list(s1 & s2)


if __name__ == "__main__":
    cases = [
        ([1, 2, 2, 1], [2, 2], {2}),
        ([4, 9, 5], [9, 4, 9, 8, 4], {4, 9}),
        ([], [1, 2], set()),
        ([1, 2, 3], [4, 5, 6], set()),
    ]
    for n1, n2, expected in cases:
        got = set(intersection(n1, n2))
        assert got == expected, f"FAIL {n1} {n2}: got {got}, expected {expected}"
    print("All tests passed.")
