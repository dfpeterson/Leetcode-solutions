"""
Level: Easy
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Tags: linked-list, math
Description:
Given head which is a reference node to a singly-linked list. The value of each
node in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = head.val
        next_head = head.next
        while next_head:
            ans <<= 1
            ans += next_head.val
            next_head = next_head.next
        return ans