/*
Level: Medium
Link: https://leetcode.com/problems/restaurant-growth/
Tags: database
Description:
You are the restaurant owner and you want to analyze a possible expansion
(there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window
(i.e., current day + 6 days before). average_amount should be rounded to two
decimal places.

Return the result table ordered by visited_on in ascending order.
*/
WITH daily_tally AS (
    SELECT
        c.visited_on,
        sum(c.amount) AS day_amt,
        count(c.amount) AS count_amt
    FROM
        customer AS c
    GROUP BY
        c.visited_on
),

moving_window AS (
    SELECT
        visited_on,
        sum(day_amt) OVER (
            ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        round(sum(day_amt) OVER (
            ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7,
        2) AS average_amount,
        count(day_amt) OVER (
            ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS rolling_count
    FROM
        daily_tally
)

SELECT
    visited_on,
    amount,
    average_amount
FROM
    moving_window
WHERE
    rolling_count >= 7
