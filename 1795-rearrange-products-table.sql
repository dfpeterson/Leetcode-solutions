/*
Level: Easy
Link: https://leetcode.com/problems/rearrange-products-table/
Tags: database
Description:
Write a solution to rearrange the Products table so that each row has
(product_id, store, price). If a product is not available in a store, do not
include a row with that product_id and store combination in the result table.

Return the result table in any order.
*/
SELECT
    p.product_id,
    'store1' AS store,
    p.store1 AS price
FROM
    products AS p
WHERE
    p.store1 IS NOT null
UNION ALL
SELECT
    p.product_id,
    'store2' AS store,
    p.store2
FROM
    products AS p
WHERE
    p.store2 IS NOT null
UNION ALL
SELECT
    p.product_id,
    'store3' AS store,
    p.store3
FROM
    products AS p
WHERE
    p.store3 IS NOT null
