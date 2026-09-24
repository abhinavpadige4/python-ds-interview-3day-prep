"""
LeetCode 933 — Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

Implement the RecentCounter class:
    - ping(t): Add a ping at time `t` and return the number of pings
      that have happened in the past 3000 milliseconds (inclusive of t).
    It is guaranteed that t is non-decreasing across calls.

Example:
    ping(1)   -> 1
    ping(100) -> 2
    ping(3001)-> 3
    ping(3002)-> 3

Approach: Queue (deque).
    - Append t, then pop from the left while the front is < t - 2999.

Time:  O(1) amortized per ping.
Space: O(n)
"""

from collections import deque
from typing import Deque


class RecentCounter:
    def __init__(self):
        self.q: Deque[int] = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 2999:
            self.q.popleft()
        return len(self.q)


if __name__ == "__main__":
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
    print("All tests passed.")
