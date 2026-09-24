# Python Data Structures Cheatsheet

## Big-O reference

| Operation | List | Tuple | Set | Dict | Deque | Heap |
|-----------|------|-------|-----|------|-------|------|
| Access by index | O(1) | O(1) | — | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(1) | O(1) | O(n) | O(n) |
| Insert (end) | O(1)* | — | O(1) | O(1) | O(1) | O(log n) |
| Insert (start) | O(n) | — | O(1) | O(1) | O(1) | O(log n) |
| Delete (end) | O(1) | — | O(1) | O(1) | O(1) | O(log n) |
| Delete (start) | O(n) | — | O(1) | O(1) | O(1) | O(log n) |
| Delete (by value) | O(n) | — | O(1) | O(1) | O(n) | O(n) |

*Amortized O(1) for list append.

## `collections` essentials

```python
from collections import deque, Counter, defaultdict, namedtuple

# deque — O(1) append/pop on both ends
dq = deque([1, 2, 3])
dq.append(4)          # right
dq.appendleft(0)      # left
dq.popleft()          # left
dq.pop()              # right

# Counter — frequency map
c = Counter("abracadabra")
c.most_common(3)      # [('a', 5), ('b', 2), ('r', 2)]

# defaultdict — auto-init missing keys
d = defaultdict(list)
d["key"].append(1)    # no KeyError

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
```

## `heapq` essentials (min-heap only)

```python
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappop(h)      # 1 (smallest)
h[0]                  # peek smallest

# Max-heap trick: negate values
heapq.heappush(h, -x)
-heapq.heappop(h)

# Top-K largest: keep a min-heap of size K
heapq.nlargest(k, iterable)
heapq.nsmallest(k, iterable)
```

## `bisect` essentials (sorted-list ops)

```python
import bisect

a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)   # 2 (first index where 5 could go)
bisect.bisect_right(a, 5)  # 3
bisect.insort(a, 4)        # a becomes [1, 3, 4, 5, 7, 9]
```

## Common templates

### Two-pointer (in-place)
```python
def solve(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        # ...
        i += 1
        j -= 1
```

### Sliding window
```python
def solve(nums, target):
    left = 0
    window_sum = 0
    best = float("inf")
    for right, val in enumerate(nums):
        window_sum += val
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return best if best != float("inf") else 0
```

### Fast/slow pointers (linked list)
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Tree DFS
```python
def dfs(node):
    if not node:
        return
    # process node
    dfs(node.left)
    dfs(node.right)
```

### Tree BFS (level order)
```python
from collections import deque
def bfs(root):
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        # process level
```

## Edge cases to always check

- Empty input (`[]`, `""`, `None`)
- Single element
- All duplicates
- Already sorted / reverse sorted
- Negative numbers
- Integer overflow (not in Python, but interviewer may ask)
- Tree: `None` root, single node, skewed tree
