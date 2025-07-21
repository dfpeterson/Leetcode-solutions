"""
Level: Hard
Link: https://leetcode.com/problems/delete-duplicate-folders-in-system/
Tags: array, hash-table, string, trie, hash-function
Description:
Due to a bug, there are many duplicate folders in a file system. You are given
a 2D array paths, where paths[i] is an array representing an absolute path to
the ith folder in the file system.
 * For example, ["one", "two", "three"] represents the path "/one/two/three".

Two folders (not necessarily on the same level) are identical if they contain
the same non-empty set of identical subfolders and underlying subfolder
structure. The folders do not need to be at the root level to be identical. If
two or more folders are identical, then mark the folders as well as all their
subfolders.
 * For example, folders "/a" and "/b" in the file structure below are
   identical. They (as well as their subfolders) should all be marked:
    * /a
    * /a/x
    * /a/x/y
    * /a/z
    * /b
    * /b/x
    * /b/x/y
    * /b/z
 * However, if the file structure also included the path "/b/w", then the
   folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x"
   would still be considered identical even with the added folder.

Once all the identical folders and their subfolders have been marked, the file
system will delete all of them. The file system only runs the deletion once, so
any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after
deleting all the marked folders. The paths may be returned in any order.
"""
from collections import Counter
class Solution:
    class Trie:
        def __init__(self):
            self.path = ''
            self.children = {}

    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = self.Trie()
        for path in paths:
            current = root
            for folder in path:
                if folder not in current.children:
                    current.children[folder] = self.Trie()
                current = current.children[folder]
        frequency = Counter()
        def construct(node):
            if not node.children:
                return
            v = []
            for parent, child in node.children.items():
                construct(child)
                v.append(f'{parent}({child.path})')
            v.sort()
            node.path = ''.join(v)
            frequency[node.path] += 1
        construct(root)
        ans = []
        path = []
        def operate(node):
            if frequency[node.path] > 1:
                return
            if path:
                ans.append(path[:])
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()
        operate(root)
        return ans