/*
Level: Medium
Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
Tags: database
Description:
Write a solution to find the people who have the most friends and the most
friends number.

The test cases are generated so that only one person has the most friends.
*/
WITH combined AS (
    SELECT r.requester_id AS id
    FROM
        requestaccepted AS r
    UNION ALL
    SELECT r.accepter_id
    FROM
        requestaccepted AS r
)

SELECT
    id,
    count(id) AS num
FROM
    combined
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1
