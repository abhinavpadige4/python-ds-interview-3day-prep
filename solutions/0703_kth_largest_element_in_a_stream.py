"""
LeetCode 703 — Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the k-th largest element in a stream of integers.

Example:
    KthLargest(3, [4, 5, 8, 2])
    add(3) -> 4
    add(5) -> 5
    add(10) -> 5
    add(9)  -> 8
    add(4)  -> 8

Approach: Min-heap of size k.
    - Keep only the k largest elements seen so far.
    - The heap root is the k-th largest.

Time:  O(log k) per add.
Space: O(k)
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap: List[int] = []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    k = KthLargest(3, [4, 5, 8, 2])
    assert k.add(3) == 4
    assert k.add(5) == 5
    assert k.add(10) == 5
    assert k.add(9) == 8
    assert k.add(4) == 8
    print("All tests passed.")
