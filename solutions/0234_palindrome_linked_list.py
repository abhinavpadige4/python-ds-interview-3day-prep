"""
LeetCode 234 — Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return True if it is a palindrome.

Example:
    Input:  head = [1,2,2,1]
    Output: True

Approach: Fast/slow pointers + reverse second half.
    - Use fast/slow to find the middle.
    - Reverse the second half.
    - Compare the two halves.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    """Return True if the linked list is a palindrome."""
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    slow.next = None
    prev = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Compare
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


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


if __name__ == "__main__":
    cases = [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
    ]
    for vals, expected in cases:
        got = is_palindrome(_build(vals))
        assert got == expected, f"FAIL {vals}: got {got}, expected {expected}"
    print("All tests passed.")
