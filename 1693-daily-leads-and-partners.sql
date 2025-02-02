/*
Level: Easy
Link: https://leetcode.com/problems/daily-leads-and-partners/
Tags: database
Description:
For each date_id and make_name, find the number of distinct lead_id's and
distinct partner_id's.

Return the result table in any order.
*/
SELECT
    ds.date_id,
    ds.make_name,
    count(DISTINCT ds.lead_id) AS unique_leads,
    count(DISTINCT ds.partner_id) AS unique_partners
FROM
    dailysales AS ds
GROUP BY
    ds.date_id,
    ds.make_name
