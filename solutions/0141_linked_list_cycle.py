"""
LeetCode 141 — Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given the head of a linked list, determine if the linked list has a cycle
in it. A cycle exists if some node can be reached again by following next
pointers.

Example:
    Input:  head = [3,2,0,-4], pos = 1
    Output: True   (tail connects to index 1)

Approach: Floyd's tortoise & hare.
    - Slow moves 1 step, fast moves 2 steps.
    - If there's a cycle, they must meet; otherwise fast reaches None.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Return True if the linked list has a cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    # No cycle
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next, b.next = b, c
    assert has_cycle(a) is False

    # With cycle: 1 -> 2 -> 3 -> 2
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next, b.next, c.next = b, c, b
    assert has_cycle(a) is True

    # Single node
    assert has_cycle(ListNode(1)) is False
    assert has_cycle(None) is False
    print("All tests passed.")
