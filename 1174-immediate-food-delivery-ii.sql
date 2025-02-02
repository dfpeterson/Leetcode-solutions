/*
Level: Medium
Link: https://leetcode.com/problems/immediate-food-delivery-ii/
Tags: database
Description:
If the customer's preferred delivery date is the same as the order date, then
the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that
the customer made. It is guaranteed that a customer has precisely one first
order.

Write a solution to find the percentage of immediate orders in the first orders
of all customers, rounded to 2 decimal places.
*/
WITH first_order AS (
    SELECT
        d.customer_id,
        (d.order_date = d.customer_pref_delivery_date)::int AS is_immediate,
        row_number() OVER (
            PARTITION BY d.customer_id
            ORDER BY
                d.order_date
        ) AS is_first
    FROM
        delivery AS d
)

SELECT
    round(
        100 * avg(fo.is_immediate)::numeric,
        2
    ) AS immediate_percentage
FROM
    first_order AS fo
WHERE
    fo.is_first = 1
