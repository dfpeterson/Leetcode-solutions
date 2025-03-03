"""
Level: Medium
Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/
Tags: array, tree, depth-first-search, binary-tree, graph
Description:
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at
node 0. You are given a 2D integer array edges of length n - 1 where
edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in
the tree.

At every node i, there is a gate. You are also given an array of even integers
amount, where amount[i] represents:
 * the price needed to open the gate at node i, if amount[i] is negative, or,
 * the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:
 * Initially, Alice is at node 0 and Bob is at node bob.
 * At every second, Alice and Bob each move to an adjacent node. Alice moves
   towards some leaf node, while Bob moves towards node 0.
 * For every node along their path, Alice and Bob either spend money to open
   the gate at that node, or accept the reward. Note that:
   * If the gate is already open, no price will be required, nor will there be
     any cash reward.
   * If Alice and Bob reach the node simultaneously, they share the
     price/reward for opening the gate there. In other words, if the price to
     open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if
     the reward at the gate is c, both of them receive c / 2 each.
 * If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches
   node 0, he stops moving. Note that these events are independent of each
   other.

Return the maximum net income Alice can have if she travels towards the optimal
leaf node.
"""
from collections import deque
class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        bob_path = {}
        edgy = {}
        for a, b in edges:
            edgy[a] = edgy.get(a, []) + [b]
            edgy[b] = edgy.get(b, []) + [a]

        def pathfinder(node, parent, step):
            if node == 0:
                bob_path[node] = step
                return True

            for neighbor in edgy[node]:
                if neighbor == parent:
                    continue
                if pathfinder(neighbor, node, step + 1):
                    bob_path[node] = step
                    return True
            return False
        
        pathfinder(bob, -1, 0)
        alice = deque([(0, 0, -1, amount[0])])
        max_profit = float('-inf')
        while alice:
            node, time, parent, profit = alice.popleft()
            for neighbor in edgy[node]:
                if neighbor == parent:
                    continue
                neighbor_profit = amount[neighbor]
                if neighbor in bob_path:
                    if time + 1 > bob_path[neighbor]:
                        neighbor_profit = 0
                    elif time + 1 == bob_path[neighbor]:
                        neighbor_profit = neighbor_profit // 2
                alice.append((neighbor, time + 1, node, profit + neighbor_profit))
                if len(edgy[neighbor]) == 1:
                    max_profit = max(max_profit, profit + neighbor_profit)
        return max_profit