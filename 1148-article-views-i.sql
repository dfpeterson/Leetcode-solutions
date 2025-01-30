/*
Level: Easy
Link: https://leetcode.com/problems/article-views-i/
Tags: database
Description:
Write a solution to find all the authors that viewed at least one of their own
articles.

Return the result table sorted by id in ascending order.
*/
SELECT v.author_id AS id
FROM
    views AS v
WHERE
    v.author_id = v.viewer_id
GROUP BY
    v.author_id
