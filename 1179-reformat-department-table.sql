/*
Level: Easy
Link: https://leetcode.com/problems/reformat-department-table/
Tags: database
Description:
Reformat the table such that there is a department id column and a revenue
column for each month.

Return the result table in any order.
*/
SELECT
    d.id,
    SUM(CASE WHEN d.month = 'Jan' THEN d.revenue END) AS jan_revenue,
    SUM(CASE WHEN d.month = 'Feb' THEN d.revenue END) AS feb_revenue,
    SUM(CASE WHEN d.month = 'Mar' THEN d.revenue END) AS mar_revenue,
    SUM(CASE WHEN d.month = 'Apr' THEN d.revenue END) AS apr_revenue,
    SUM(CASE WHEN d.month = 'May' THEN d.revenue END) AS may_revenue,
    SUM(CASE WHEN d.month = 'Jun' THEN d.revenue END) AS jun_revenue,
    SUM(CASE WHEN d.month = 'Jul' THEN d.revenue END) AS jul_revenue,
    SUM(CASE WHEN d.month = 'Aug' THEN d.revenue END) AS aug_revenue,
    SUM(CASE WHEN d.month = 'Sep' THEN d.revenue END) AS sep_revenue,
    SUM(CASE WHEN d.month = 'Oct' THEN d.revenue END) AS oct_revenue,
    SUM(CASE WHEN d.month = 'Nov' THEN d.revenue END) AS nov_revenue,
    SUM(CASE WHEN d.month = 'Dec' THEN d.revenue END) AS dec_revenue
FROM
    department AS d
GROUP BY
    d.id
/* Checking the solutions after I saw one that used FILTER(WHERE ...) instead
	of CASE WHEN and I like that more than my solution.
*/
