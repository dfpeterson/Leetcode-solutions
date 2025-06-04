"""
Level: Hard
Link: https://leetcode.com/problems/candy/
Tags: array, greedy
Description:
There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings.

You are giving candies to these children subjected to the following
requirements:
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies
to the children.
"""
class Solution:
    def candy(self, ratings: list[int]) -> int:
        ans = [1]
        reverse = 0
        for i in range(1, len(ratings)):
            if ratings[i - 1] <= ratings[i]:
                ans.append(1 if ratings[i - 1] == ratings[i] else ans[i - 1] + 1)
                if reverse:
                    j = i - 1
                    while j > 0 and ratings[j - 1] > ratings[j]:
                        if ans[j] + 1 > ans[j - 1]:
                            ans[j - 1] = ans[j] + 1
                            j -= 1
                        else:
                            j = 0
            else:
                ans.append(1)
                reverse += 1
        if reverse:
            j = i
            while j > 0 and ratings[j - 1] > ratings[j]:
                if ans[j] + 1 > ans[j - 1]:
                    ans[j - 1] = ans[j] + 1
                    j -= 1
                else:
                    j = 0
        return sum(ans)
