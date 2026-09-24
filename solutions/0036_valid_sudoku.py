"""
LeetCode 36 — Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:
    1. Each row must contain digits 1-9 without duplicates.
    2. Each column must contain digits 1-9 without duplicates.
    3. Each of the nine 3x3 sub-boxes must contain digits 1-9 without
       duplicates.

Example:
    Input:  [["5","3",".",".","7",".",".",".","."], ...]
    Output: True

Approach: Hash sets.
    - Maintain 9 row sets, 9 col sets, 9 box sets.
    - For each filled cell, check membership; if duplicate, return False.

Time:  O(81) = O(1)
Space: O(81) = O(1)
"""

from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """Return True if the 9x9 Sudoku board is valid."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    return True


if __name__ == "__main__":
    valid = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    assert is_valid_sudoku(valid) is True
    # Invalid: duplicate 5 in first row
    invalid = [row[:] for row in valid]
    invalid[0][1] = "5"
    assert is_valid_sudoku(invalid) is False
    print("All tests passed.")
