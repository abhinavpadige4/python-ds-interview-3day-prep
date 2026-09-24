"""
LeetCode 232 — Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first-in-first-out (FIFO) queue using only two stacks.
The queue should support all standard operations: push, pop, peek, empty.

Example:
    push(1); push(2); peek() -> 1; pop() -> 1; empty() -> False

Approach: Two stacks.
    - `in_stack` receives pushes.
    - `out_stack` serves pops; when empty, transfer all from in_stack.
    - Amortized O(1) per operation.

Time:  O(1) amortized per operation.
Space: O(n)
"""

from typing import List


class MyQueue:
    def __init__(self):
        self.in_stack: List[int] = []
        self.out_stack: List[int] = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    print("All tests passed.")
