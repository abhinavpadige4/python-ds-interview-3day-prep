"""
LeetCode 206 — Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list and return the
new head.

Example:
    Input:  head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Approach: Iterative three-pointer reversal.
    - `prev` starts at None, `curr` at head.
    - For each node, save next, point curr.next to prev, advance both.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse the linked list in-place and return the new head."""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def _build(vals):
    head = None
    tail = None
    for v in vals:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
    ]
    for vals, expected in cases:
        head = _build(vals)
        got = _to_list(reverse_list(head))
        assert got == expected, f"FAIL {vals}: got {got}, expected {expected}"
    print("All tests passed.")
