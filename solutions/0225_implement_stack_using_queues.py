"""
LeetCode 225 — Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Implement a last-in-first-out (LIFO) stack using only two queues.
Support push, pop, top, empty.

Example:
    push(1); push(2); top() -> 2; pop() -> 2; empty() -> False

Approach: Two queues.
    - On push, rotate the existing queue so the new element is at the front.
    - pop/top just operate on the front of the primary queue.

Time:  O(n) for push, O(1) for pop/top/empty.
Space: O(n)
"""

from collections import deque
from typing import Deque


class MyStack:
    def __init__(self):
        self.q1: Deque[int] = deque()
        self.q2: Deque[int] = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.empty() is False
    assert s.pop() == 1
    assert s.empty() is True
    print("All tests passed.")
