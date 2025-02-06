/*
Level: Medium
Link: https://leetcode.com/problems/product-price-at-a-given-date/
Tags: database
Description:
Write a solution to find the prices of all products on 2019-08-16. Assume the
price of all products before any change is 10.

Return the result table in any order.
*/
WITH price_changes AS (
    SELECT
        p.product_id,
        p.new_price,
        p.change_date,
        CASE
            WHEN ('2019-08-16' - p.change_date) < 0 THEN null
            ELSE '2019-08-16' - p.change_date
        END AS days_diff,
        min(
            CASE
                WHEN ('2019-08-16' - p.change_date) < 0 THEN null ELSE
                    '2019-08-16' - p.change_date
            END
        ) OVER (PARTITION BY p.product_id) AS min_days_diff
    FROM
        products AS p
)

SELECT
    product_id,
    CASE
        WHEN min_days_diff IS null THEN 10
        ELSE new_price
    END AS price
FROM
    price_changes
WHERE
    days_diff = min_days_diff
    OR min_days_diff IS null
GROUP BY
    product_id,
    CASE
        WHEN min_days_diff IS null THEN 10
        ELSE new_price
    END
