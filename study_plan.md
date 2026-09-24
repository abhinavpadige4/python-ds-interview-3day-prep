# 3-Day Python Data Structures Interview Prep

**Dates:** 2026-09-25 → 2026-09-27
**Notion tracker:** https://app.notion.com/p/Python-Data-Structures-Interview-Prep-3-Day-Plan-3e540c05b27981dd8649f4423ec67294

## Ground rules

- **25–30 min cap per problem.** If you're stuck, read the editorial, then re-implement from scratch.
- **Speak out loud** while coding — interviewers grade communication, not just correctness.
- **Every solution must include:** approach, code, time complexity, space complexity, edge cases.
- **Breaks are mandatory.** 15 min every 90 min. No skipping.

---

## Day 1 — 2026-09-25 — Arrays, Strings, Sets, Dicts

| Time | Activity |
|------|----------|
| 09:00–09:30 | Review Python lists, tuples, strings — https://docs.python.org/3/tutorial/datastructures.html |
| 09:30–09:45 | Break |
| 09:45–11:15 | Practice: 283, 26, 27, 977, 209 |
| 11:15–12:00 | Review solutions, note patterns (two-pointer, sliding window) |
| 12:00–13:00 | Lunch |
| 13:00–13:30 | Review sets & dicts — https://realpython.com/python-sets/ , https://realpython.com/python-dicts/ |
| 13:30–14:30 | Practice: 349, 202, 1, 36, 380 |
| 14:30–14:45 | Break |
| 14:45–16:00 | Continue practice, review hash-map patterns |
| 16:00–16:30 | Flashcards: key methods + time complexities (Anki) |
| 16:30–17:00 | Wrap-up, note weak areas |

**Day 1 patterns to internalize:**
- Two-pointer (283, 26, 27, 977)
- Sliding window (209)
- Hash-set membership (349, 202)
- Hash-map lookup (1, 36)
- List + hash-set hybrid for O(1) ops (380)

---

## Day 2 — 2026-09-26 — Stacks, Queues, Heaps, Bisect

| Time | Activity |
|------|----------|
| 09:00–09:30 | Review `collections.deque`, `Counter`, `defaultdict`, `namedtuple` — https://docs.python.org/3/library/collections.html |
| 09:30–09:45 | Break |
| 09:45–11:15 | Practice: 232, 225, 933, 20, 155 |
| 11:15–12:00 | Review stack/queue patterns |
| 12:00–13:00 | Lunch |
| 13:00–13:30 | Review `heapq` — https://docs.python.org/3/library/heapq.html |
| 13:30–15:00 | Practice: 621, 703, 215, 347, 1005 |
| 15:00–15:15 | Break |
| 15:15–16:30 | Review heap patterns, redo any missed problems |
| 16:30–17:00 | Flashcards + wrap-up |

**Day 2 patterns to internalize:**
- Stack for matching/nesting (20, 155)
- Queue via `deque` (933, 225)
- Stack-as-queue and vice versa (232, 225)
- Min-heap for top-K (703, 215, 347)
- Greedy + heap (621, 1005)

---

## Day 3 — 2026-09-27 — Linked Lists, Trees, Mock Interview

| Time | Activity |
|------|----------|
| 09:00–09:30 | Review linked-list node template + tree node template |
| 09:30–09:45 | Break |
| 09:45–11:15 | Practice: 206, 21, 141, 234 |
| 11:15–12:00 | Review linked-list patterns (dummy head, fast/slow) |
| 12:00–13:00 | Lunch |
| 13:00–13:30 | Review tree traversals (DFS/BFS) |
| 13:30–15:00 | Practice: 104, 226, 101, 94, 102, 199 |
| 15:00–15:15 | Break |
| 15:15–16:30 | **Mock interview** — pick 2 random problems from the 30, 45 min each, record yourself |
| 16:30–17:00 | Debrief: what tripped you up? Update Notion tracker. |

**Day 3 patterns to internalize:**
- Iterative + recursive reversal (206)
- Merge pattern (21)
- Fast/slow pointers (141, 234)
- DFS recursion (104, 226, 101, 94)
- BFS with `deque` (102, 199)

---

## Mock interview rubric (Day 3)

Score each of the 2 problems 0–5 on:

1. **Problem understanding** — did you restate the problem and clarify edge cases?
2. **Approach articulation** — did you explain the algorithm before coding?
3. **Code quality** — clean, idiomatic Python, no obvious bugs?
4. **Complexity analysis** — correct time + space?
5. **Testing** — did you walk through at least one example by hand?

**Target: ≥ 18/20 across both problems.**

---

## Final checklist before the interview

- [ ] All 30 solutions re-implemented from memory at least once
- [ ] `cheatsheet.md` memorized (Big-O table + `collections`/`heapq`/`bisect` APIs)
- [ ] Notion tracker updated with weak areas
- [ ] Mock interview recorded and reviewed
- [ ] Sleep ≥ 7 hours the night before
