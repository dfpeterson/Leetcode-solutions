"""
Level: Hard
Link: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
Tags: array, breadth-first-search, graph
Description:
You have n boxes labeled from 0 to n - 1. You are given four arrays: status,
candies, keys, and containedBoxes where:
 * status[i] is 1 if the ith box is open and 0 if the ith box is closed,
 * candies[i] is the number of candies in the ith box,
 * keys[i] is a list of the labels of the boxes you can open after opening the
   ith box.
 * containedBoxes[i] is a list of the boxes you found inside the ith box.

You are given an integer array initialBoxes that contains the labels of the
boxes you initially have. You can take all the candies in any open box and you
can use the keys in it to open new boxes and you also can use the boxes you
find in it.

Return the maximum number of candies you can get following the rules above.
"""
class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        N = len(candies)
        ans = 0
        head = 0
        checked = [False] * N
        all_boxes = [False] * N
        openable = status.copy()
        q = []
        for box in initialBoxes:
            all_boxes[box] = True
            if openable[box] and not checked[box]:
                q.append(box)
                checked[box] = True
        while head < len(q):
            current_box = q[head]
            head += 1
            ans += candies[current_box]
            for key in keys[current_box]:
                if not openable[key]:
                    openable[key] = 1
                if all_boxes[key] and openable[key] and not checked[key]:
                    q.append(key)
                    checked[key] = True
            for box2 in containedBoxes[current_box]:
                all_boxes[box2] = True
                if openable[box2] and not checked[box2]:
                    q.append(box2)
                    checked[box2] = True

        return ans