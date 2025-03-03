"""
Level: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
Tags: array, hash-table, divide-and-conquer, tree, binary-tree
Description:
Given two integer arrays, preorder and postorder where preorder is the preorder
traversal of a binary tree of distinct values and postorder is the postorder
traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        branches = len(preorder)
        post_order_vals = {n: m for m, n in enumerate(postorder)}

        def tree_construct(i1, i2, j):
            if i1 > i2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_value = preorder[i1 + 1]
                mid = post_order_vals[left_value]
                left_branch = mid - j + 1
                root.left = tree_construct(i1 + 1, i1 + left_branch, j)
                root.right = tree_construct(i1 + left_branch + 1, i2, mid + 1)
            return root

        return tree_construct(0, branches - 1, 0)