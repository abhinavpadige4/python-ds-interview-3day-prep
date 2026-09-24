"""
LeetCode 380 — Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Implement the RandomizedSet class:
    - insert(val): Insert val if not present. Return True if inserted.
    - remove(val): Remove val if present. Return True if removed.
    - getRandom(): Return a random element from the current set, each
      element equally likely.
All operations must run in O(1) average time.

Approach: List + hash map.
    - `nums` list stores values for O(1) random access.
    - `index` map stores value -> position in `nums`.
    - To remove: swap the target with the last element, pop, update map.

Time:  O(1) average for all operations.
Space: O(n)
"""

import random
from typing import List


class RandomizedSet:
    def __init__(self):
        self.nums: List[int] = []
        self.index: dict = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        last = self.nums[-1]
        pos = self.index[val]
        self.nums[pos] = last
        self.index[last] = pos
        self.nums.pop()
        del self.index[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    rs = RandomizedSet()
    assert rs.insert(1) is True
    assert rs.insert(2) is True
    assert rs.insert(1) is False
    assert rs.remove(1) is True
    assert rs.remove(3) is False
    assert rs.insert(2) is False
    assert rs.insert(3) is True
    for _ in range(100):
        assert rs.get_random() in (2, 3)
    print("All tests passed.")
