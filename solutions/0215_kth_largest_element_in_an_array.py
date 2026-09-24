"""
LeetCode 215 — Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array `nums` and an integer `k`, return the k-th largest
element in the array. The k-th largest means the k-th largest in the
sorted order, not the k-th distinct element.

Example:
    Input:  nums = [3,2,1,5,6,4], k = 2
    Output: 5

Approach: Min-heap of size k.
    - Push each element; if heap exceeds k, pop the smallest.
    - The heap root is the k-th largest.

Time:  O(n log k)
Space: O(k)
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """Return the k-th largest element in `nums`."""
    heap: List[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([1, 2], 1, 2),
    ]
    for nums, k, expected in cases:
        got = find_kth_largest(nums, k)
        assert got == expected, f"FAIL {nums} k={k}: got {got}, expected {expected}"
    print("All tests passed.")
