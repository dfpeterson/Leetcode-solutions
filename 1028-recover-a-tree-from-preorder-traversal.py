"""
Level: Hard
Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
Tags: string, tree, depth-first-search, binary-tree
Description:
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of
this node), then we output the value of this node.  If the depth of a node is
D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its
root.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        current_depth = 0
        depths = []
        for d in traversal.split('-'):
            if d:
                value = int(d)
                node = TreeNode(value)
                while len(depths) > current_depth:
                    depths.pop()
                if depths and not depths[-1].left:
                    depths[-1].left = node
                elif depths:
                    depths[-1].right = node
                depths.append(node)
                current_depth = 1
            else:
                current_depth += 1
        return depths[0]