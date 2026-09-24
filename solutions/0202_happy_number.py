"""
LeetCode 202 — Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number `n` is happy.
A happy number is defined by the following process:
    Starting with any positive integer, replace the number by the sum of
    the squares of its digits. Repeat until the number equals 1 (happy)
    or loops endlessly in a cycle (not happy).

Example:
    Input:  n = 19
    Output: True   (1^2 + 9^2 = 82 -> 68 -> 100 -> 1)

Approach: Floyd's cycle detection (tortoise & hare).
    - If the sequence reaches 1, it's happy.
    - Otherwise it must cycle; detect the cycle with two pointers.

Time:  O(log n) per step, bounded iterations.
Space: O(1)
"""


def is_happy(n: int) -> bool:
    """Return True if `n` is a happy number."""
    def next_num(x: int) -> int:
        total = 0
        while x:
            d = x % 10
            total += d * d
            x //= 10
        return total

    slow = n
    fast = next_num(n)
    while fast != 1 and slow != fast:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
    return fast == 1


if __name__ == "__main__":
    cases = [
        (19, True),
        (1, True),
        (2, False),
        (4, False),
        (10, True),
    ]
    for n, expected in cases:
        got = is_happy(n)
        assert got == expected, f"FAIL n={n}: got {got}, expected {expected}"
    print("All tests passed.")
