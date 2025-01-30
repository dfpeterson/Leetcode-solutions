/*
Level: Easy
Link: https://leetcode.com/problems/invalid-tweets/
Tags: database
Description:
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if
the number of characters used in the content of the tweet is strictly greater
than 15.

Return the result table in any order.
*/
SELECT t.tweet_id
FROM
    tweets AS t
WHERE
    LENGTH(t.content) > 15
