"""
LeetCode 1005 — Maximize Sum Of Array After K Negations
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

Given an integer array `nums` and an integer `k`, modify the array by
choosing any index `i` and replacing `nums[i]` with `-nums[i]`. Repeat
this exactly `k` times. Return the largest possible sum of the array.

Example:
    Input:  nums = [4,2,3], k = 1
    Output: 5   (negate 4 -> [-4,2,3], sum = 1; better: negate 2 -> [4,-2,3], sum = 5)

Approach: Min-heap.
    - Push all values into a min-heap.
    - For each of k steps, pop the smallest, negate it, push back.
    - Sum the heap at the end.

Time:  O((n + k) log n)
Space: O(n)
"""

import heapq
from typing import List


def largest_sum_after_negations(nums: List[int], k: int) -> int:
    """Return the maximum possible sum after exactly k negations."""
    heap = list(nums)
    heapq.heapify(heap)
    for _ in range(k):
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, -smallest)
    return sum(heap)


if __name__ == "__main__":
    cases = [
        ([4, 2, 3], 1, 5),
        ([3, -1, 0, 2], 3, 6),
        ([2, 3, 1, 5, 4], 3, 13),
        ([-1], 1, 1),
    ]
    for nums, k, expected in cases:
        got = largest_sum_after_negations(nums, k)
        assert got == expected, f"FAIL {nums} k={k}: got {got}, expected {expected}"
    print("All tests passed.")
