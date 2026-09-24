"""
LeetCode 621 — Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a list of tasks represented by uppercase letters and a cooldown
interval `n`, return the minimum number of slots needed to complete all
tasks. In each slot you can either complete one task or idle.

Example:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8   (A -> idle -> idle -> B -> A -> idle -> idle -> B)

Approach: Greedy + counting.
    - Count frequencies.
    - The bottleneck is the most frequent task: it forces
      (max_freq - 1) * (n + 1) + (number of tasks tied at max_freq) slots.
    - Answer is max(len(tasks), that expression).

Time:  O(n)
Space: O(1) (26 letters)
"""

from collections import Counter
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """Return the minimum number of slots to schedule all tasks with cooldown n."""
    counts = Counter(tasks)
    max_freq = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)


if __name__ == "__main__":
    cases = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "A", "C"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A"], 5, 1),
    ]
    for tasks, n, expected in cases:
        got = least_interval(tasks, n)
        assert got == expected, f"FAIL {tasks} n={n}: got {got}, expected {expected}"
    print("All tests passed.")
