/*
Level: Medium
Link: https://leetcode.com/problems/exchange-seats/
Tags: database
Description:
Write a solution to swap the seat id of every two consecutive students. If the
number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
*/
WITH seat_rearrange AS (
    SELECT
        s.id,
        s.student,
        coalesce(CASE
            WHEN s.id % 2 = 1
                THEN lead(s.id) OVER (
                    ORDER BY s.id
                )
            ELSE lag(s.id) OVER (
                ORDER BY s.id
            )
        END,
        s.id) AS new_seat
    FROM
        seat AS s
)

SELECT
    new_seat AS id,
    student
FROM
    seat_rearrange
ORDER BY
    new_seat
