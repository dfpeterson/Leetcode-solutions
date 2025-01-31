/*
Level: Easy
Link: https://leetcode.com/problems/product-sales-analysis-i/
Tags: database
Description:
Write a solution to report the product_name, year, and price for each sale_id
in the Sales table.

Return the resulting table in any order.
*/
SELECT
    p.product_name,
    s.year,
    s.price
FROM
    sales AS s
INNER JOIN product AS p ON
    s.product_id = p.product_id
