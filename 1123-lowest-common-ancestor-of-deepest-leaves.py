"""
Level: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
Tags: hash-table, tree, depth-first-search, breadth-first-search, binary-tree
Description:
Given the root of a binary tree, return the lowest common ancestor of its
deepest leaves.
Recall that:
 * The node of a binary tree is a leaf if and only if it has no children
 * The depth of the root of the tree is 0. if the depth of a node is d, the
   depth of each of its children is d + 1.
 * The lowest common ancestor of a set S of nodes, is the node A with the
   largest depth such that every node in S is in the subtree with root A.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def node_check(node):
            if not node:
                return (None, 0)
            left_node, left_height = node_check(node.left)
            right_node, right_height = node_check(node.right)

            if left_height > right_height:
                return (left_node, left_height + 1)
            elif left_height < right_height:
                return (right_node, right_height + 1)
            return (node, left_height + 1)

        ans = node_check(root)
        return ans[0]