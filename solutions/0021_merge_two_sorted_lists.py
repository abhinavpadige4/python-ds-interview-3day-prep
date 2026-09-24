"""
LeetCode 21 — Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list. The new
list should be made by splicing together the nodes of the first two lists.

Example:
    Input:  l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Approach: Dummy head + two-pointer merge.
    - Use a dummy node to avoid special-casing the head.
    - At each step, attach the smaller of the two current nodes.

Time:  O(m + n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list."""
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [1], [1]),
        ([1], [2], [1, 2]),
    ]
    for a, b, expected in cases:
        got = _to_list(merge_two_lists(_build(a), _build(b)))
        assert got == expected, f"FAIL {a} {b}: got {got}, expected {expected}"
    print("All tests passed.")
