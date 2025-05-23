/*
Level: Medium
Link: https://leetcode.com/problems/last-person-to-fit-in-the-bus/
Tags: database
Description:
There is a queue of people waiting to board a bus. However, the bus has a
weight limit of 1000 kilograms, so there may be some people who cannot board.

Write a solution to find the person_name of the last person that can fit on the
bus without exceeding the weight limit. The test cases are generated such that
the first person does not exceed the weight limit.

Note that only one person can board the bus at any given turn.
*/
WITH weight_accrue AS (
    SELECT
        q.person_name,
        q.turn,
        sum(q.weight) OVER (
            ORDER BY q.turn
        ) AS cum_weight
    FROM
        queue AS q
    ORDER BY
        cum_weight DESC
)

SELECT person_name
FROM
    weight_accrue
WHERE
    cum_weight <= 1000
ORDER BY
    turn DESC
LIMIT 1
