/*
Level: Easy
Link: https://leetcode.com/problems/average-selling-price/
Tags: database
Description:
Write a solution to find the average selling price for each product.
average_price should be rounded to 2 decimal places. If a product does not have
any sold units, its average selling price is assumed to be 0.

Return the result table in any order.
*/
WITH weighted_prices AS (
    SELECT
        p.product_id,
        p.price
        * u.units
        / (
            sum(u.units) OVER (PARTITION BY p.product_id)
        )::numeric AS sales_ratio
    FROM
        unitssold AS u
    FULL JOIN prices AS p ON
        u.product_id = p.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
)

SELECT
    product_id,
    round(coalesce(
        sum(sales_ratio),
        0
    ),
    2) AS average_price
FROM
    weighted_prices
GROUP BY
    product_id
