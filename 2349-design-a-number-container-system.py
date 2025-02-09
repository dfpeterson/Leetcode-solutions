
"""
Level: Medium
Link: https://leetcode.com/problems/design-a-number-container-system/
Description:
Design a number container system that can do the following:
 * Insert or Replace a number at the given index in the system.
 * Return the smallest index for the given number in the system.

Implement the NumberContainers class:
 * NumberContainers() Initializes the number container system.
 * void change(int index, int number) Fills the container at index with the
   number. If there is already a number at that index, replace it.
 * int find(int number) Returns the smallest index for the given number, or -1
   if there is no index that is filled by number in the system.
"""
# This worked, but got a time limit exceeded. I ended up implementing a
# solution that used a sorted list, but it wasn't entirely mine
class NumberContainers:

    def __init__(self):
        self.vals = {}
        self.locs = {}

    def change(self, index: int, number: int) -> None:
        if index not in self.locs:
            self.locs[index] = number
            if number in self.vals:
                self.vals[number] = self.vals[number] | {index}
            else:
                #print(self.vals, number, index)
                self.vals[number] = {index}
                #self.vals.get(number, []).append(index)
        else:
            if self.locs[index] in self.vals:
                self.vals[self.locs[index]] = self.vals[self.locs[index]] - {index}

                #self.vals[self.locs[index]] - set(self.locs[index])
            if number in self.vals:
                self.vals[number] = self.vals[number] | {index}
            else:
                self.vals[number] = {index}
                #self.vals.get(number, []).append(index)
                #print(self.vals)

            #self.vals[number].pop(self.vals[number].index(index))
            self.locs[index] = number
            #print(self.vals, self.locs)
            #print(number, index)
            #swap

    def find(self, number: int) -> int:
        if not self.vals.get(number, None):
            return -1
        #print(self.vals, self.locs, number)
        return min(self.vals[number])


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)