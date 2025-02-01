/*
Level: Medium
Link: https://leetcode.com/problems/capital-gainloss/
Tags: database
Description:
Write a solution to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and
selling the stock one or many times.

Return the result table in any order.
*/
WITH buys AS (
    SELECT
        s.stock_name,
        s.operation,
        s.price,
        row_number() OVER (
            PARTITION BY s.stock_name
            ORDER BY
                s.operation_day
        ) AS transact_order
    FROM
        stocks AS s
    WHERE
        s.operation = 'Buy'
),

sells AS (
    SELECT
        s.stock_name,
        s.operation,
        s.price,
        row_number() OVER (
            PARTITION BY s.stock_name
            ORDER BY
                s.operation_day
        ) AS transact_order
    FROM
        stocks AS s
    WHERE
        s.operation = 'Sell'
)

SELECT
    b.stock_name,
    sum(s.price - b.price) AS capital_gain_loss
FROM
    buys AS b
INNER JOIN sells AS s
    ON
        b.stock_name = s.stock_name
        AND b.transact_order = s.transact_order
GROUP BY
    b.stock_name
