"""
Level: Medium
Link: https://leetcode.com/problems/product-of-the-last-k-numbers/
Tags: array, math, design, data-stream, prefix-sum
Description:
Design an algorithm that accepts a stream of integers and retrieves the product
of the last k integers of the stream.

Implement the ProductOfNumbers class:
 * ProductOfNumbers() Initializes the object with an empty stream.
 * void add(int num) Appends the integer num to the stream.
 * int getProduct(int k) Returns the product of the last k numbers in the
   current list. You can assume that always the current list has at least k
   numbers.

The test cases are generated so that, at any time, the product of any
contiguous sequence of numbers will fit into a single 32-bit integer without
overflowing.
"""
class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
        elif self.nums:
            self.nums.append(self.nums[-1] * num)
        else:
            self.nums.append(num)

    def getProduct(self, k: int) -> int:
        if k == len(self.nums):
            return self.nums[-1]
        elif k < len(self.nums):
            print(self.nums[-k],self.nums[-1], self.nums)
            return int(self.nums[-1]/self.nums[-k-1])
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)