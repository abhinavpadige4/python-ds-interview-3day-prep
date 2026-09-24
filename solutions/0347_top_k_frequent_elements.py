"""
LeetCode 347 — Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array `nums` and an integer `k`, return the k most
frequent elements. You may return the answer in any order.

Example:
    Input:  nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Approach: Counter + min-heap of size k.
    - Count frequencies with Counter.
    - Maintain a min-heap of (freq, value) of size k.

Time:  O(n log k)
Space: O(n)
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements in `nums`."""
    counts = Counter(nums)
    heap: List[tuple] = []
    for val, freq in counts.items():
        heapq.heappush(heap, (freq, val))
        if len(heap) > k:
            heapq.heappop(heap)
    return [val for _, val in heap]


if __name__ == "__main__":
    cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 1, -1, 2, -1, 2, 4], 2, {-1, 2}),
    ]
    for nums, k, expected in cases:
        got = set(top_k_frequent(nums, k))
        assert got == expected, f"FAIL {nums} k={k}: got {got}, expected {expected}"
    print("All tests passed.")
