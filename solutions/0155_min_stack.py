"""
LeetCode 155 — Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Example:
    push(-2); push(0); push(-3); getMin() -> -3; pop(); getMin() -> -2

Approach: Auxiliary stack tracking running minimum.
    - `stack` holds values.
    - `min_stack` holds the current minimum after each push.

Time:  O(1) for all operations.
Space: O(n)
"""

from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2
    print("All tests passed.")
