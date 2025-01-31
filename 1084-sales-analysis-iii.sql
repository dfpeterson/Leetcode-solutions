/*
Level: Easy
Link: https://leetcode.com/problems/sales-analysis-iii/
Tags: database
Description:
Write a solution to report the products that were only sold in the first
quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.
*/
-- Write your PostgreSQL query statement below
SELECT
    p.product_id,
    p.product_name
FROM
    product AS p
INNER JOIN sales AS s
    ON
        p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
HAVING
    COUNT(s.sale_date)
    = COUNT(
        CASE
            WHEN
                s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
                THEN s.sale_date
        END
    )
/* After submitting this I was browsing solutions and saw a better answer
   that used MIN() and MAX() of sale date to get at the solution, which uses
   much less calcuation than the COUNT(CASE WHEN...) version that I did.
*/ 