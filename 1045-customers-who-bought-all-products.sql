/*
Level: Medium
Link: https://leetcode.com/problems/customers-who-bought-all-products/
Tags: database
Description:
Write a solution to report the customer ids from the Customer table that bought
all the products in the Product table.

Return the result table in any order.
*/
WITH total_prods AS (
    SELECT count(*) AS total_products
    FROM
        product
)

SELECT c.customer_id
FROM
    customer AS c
INNER JOIN total_prods AS tp
    ON
        1 = 1
GROUP BY
    c.customer_id,
    tp.total_products
HAVING
    count(DISTINCT c.product_key) = tp.total_products
