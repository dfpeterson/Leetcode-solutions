/*
Level:  Easy
Link: https://leetcode.com/problems/group-sold-products-by-the-date/
Tags: database
Description:
Write a solution to find for each date the number of different products sold
and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.
*/
SELECT
    a.sell_date,
    count(DISTINCT a.product) AS num_sold,
    string_agg(
        DISTINCT a.product,
        ','
        ORDER BY
            a.product
    ) AS products
FROM
    activities AS a
GROUP BY
    a.sell_date
