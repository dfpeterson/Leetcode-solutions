/*
Level: Medium
Link: https://leetcode.com/problems/product-sales-analysis-iii/
Tags: database
Description:
Write a solution to select the product id, year, quantity, and price for the
first year of every product sold.

Return the resulting table in any order.
*/
WITH first_years AS (
    SELECT
        p.product_id,
        s.year,
        s.quantity,
        s.price,
        rank() OVER (
            PARTITION BY p.product_id
            ORDER BY
                s.year
        ) AS year_rank
    FROM
        sales AS s
    INNER JOIN product AS p ON
        s.product_id = p.product_id
)

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM
    first_years
WHERE
    year_rank = 1
