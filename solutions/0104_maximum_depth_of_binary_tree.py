"""
LeetCode 104 — Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3

Approach: DFS recursion.
    - Depth of a node = 1 + max(depth of left, depth of right).
    - Base case: None has depth 0.

Time:  O(n)
Space: O(h) recursion stack, h = tree height.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth of the binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    # [3,9,20,null,null,15,7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3

    # Single node
    assert max_depth(TreeNode(1)) == 1

    # Empty
    assert max_depth(None) == 0

    # Skewed
    skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert max_depth(skewed) == 3
    print("All tests passed.")
