"""
Level: Medium
Link: https://leetcode.com/problems/solving-questions-with-brainpower/
Tags: array, dynamic-programming
Description:
You are given a 0-indexed 2D integer array questions where
questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the
questions in order (i.e., starting from question 0) and make a decision whether
to solve or skip each question. Solving question i will earn you pointsi points
but you will be unable to solve each of the next brainpoweri questions. If you
skip question i, you get to make the decision on the next question.
 * For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
   * If question 0 is solved, you will earn 3 points but you will be unable to
     solve questions 1 and 2.
   * If instead, question 0 is skipped and question 1 is solved, you will earn
     4 points but you will be unable to solve questions 2 and 3.

Return the maximum points you can earn for the exam.
"""
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        num_questions = len(questions)
        point_bank = [0] * num_questions
        point_bank[-1] = questions[-1][0]
        for k in range(num_questions-2, -1, -1):
            if questions[k][1] + k + 1 < num_questions:
                point_bank[k] = max(point_bank[k + 1], questions[k][0] + point_bank[k + questions[k][1] + 1])
            else:
                point_bank[k] = max(point_bank[k + 1], questions[k][0])
        return max(point_bank)
