"""
LeetCode 20 — Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string `s` containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.
A string is valid if:
    - Open brackets are closed by the same type of bracket.
    - Open brackets are closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

Example:
    Input:  s = "()[]{}"
    Output: True

Approach: Stack.
    - Push open brackets onto the stack.
    - On a close bracket, pop and check for a matching pair.
    - Valid iff the stack is empty at the end.

Time:  O(n)
Space: O(n)
"""


def is_valid(s: str) -> bool:
    """Return True if the bracket string `s` is valid."""
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
    ]
    for s, expected in cases:
        got = is_valid(s)
        assert got == expected, f"FAIL s={s!r}: got {got}, expected {expected}"
    print("All tests passed.")
