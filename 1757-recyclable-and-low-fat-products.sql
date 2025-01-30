/*
Level: Easy
Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
Tags: database
Description:
Write a solution to find the ids of products that are both low fat and
recyclable.

Return the result table in any order.
*/
SELECT p.product_id
FROM
    products AS p
WHERE
    p.low_fats = 'Y'
    AND p.recyclable = 'Y'
