"""
Level: Medium
Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
Tags: hash-table, tree, depth-first-search, breadth-first-search, design, binary-tree
Description:
Given a binary tree with the following rules:
 1. root.val == 0
 2. For any treeNode:
    1. If treeNode.val has a value x and treeNode.left != null, then
       treeNode.left.val == 2 * x + 1
    2. If treeNode.val has a value x and treeNode.right != null, then
       treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been
changed to -1.

Implement the FindElements class:
 * FindElements(TreeNode* root) Initializes the object with a contaminated
   binary tree and recovers it.
 * bool find(int target) Returns true if the target value exists in the
   recovered binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.construct = set()
        traversing = deque()
        traversing.append((0, root))
        while traversing:
            contam_node = traversing.popleft()
            x = contam_node[0]
            if contam_node[1]:
                traversing.append(((2*x)+1, contam_node[1].left))
                traversing.append(((2*x)+2, contam_node[1].right))
                self.construct.add(x)

    def find(self, target: int) -> bool:
        return target in self.construct


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)