/*
Level: Hard
Link: https://leetcode.com/problems/human-traffic-of-stadium/
Tags: database
Description:
Write a solution to display the records with three or more rows with
consecutive id's, and the number of people is greater than or equal to 100 for
each.

Return the result table ordered by visit_date in ascending order.
*/
WITH traffic AS (
    SELECT
        s.id,
        s.visit_date,
        s.people,
        coalesce((
            s.people >= 100
            AND lead(s.people) OVER (
                ORDER BY s.visit_date
            ) >= 100
            AND lead(
                s.people,
                2)
                OVER (
                    ORDER BY s.visit_date
                )
            >= 100
        )
        OR (
            s.people >= 100
            AND lag(s.people) OVER (
                ORDER BY s.visit_date
            ) >= 100
            AND lag(
                s.people,
                2)
                OVER (
                    ORDER BY s.visit_date
                )
            >= 100
        )
        OR (
            s.people >= 100
            AND lag(s.people) OVER (
                ORDER BY s.visit_date
            ) >= 100
            AND lead(s.people) OVER (
                ORDER BY s.visit_date
            ) >= 100
        ), FALSE) AS consec_days
    FROM
        stadium AS s
)

SELECT
    id,
    visit_date,
    people
FROM
    traffic
WHERE
    consec_days
ORDER BY
    visit_date
