/*
Level: Medium
Link: https://leetcode.com/problems/investments-in-2016/
Tags: database
Description:
Write a solution to report the sum of all total investment values in 2016
tiv_2016, for all policyholders who:
 * have the same tiv_2015 value as one or more other policyholders, and
 * are not located in the same city as any other policyholder (i.e., the (lat,
   lon) attribute pairs must be unique).

Round tiv_2016 to two decimal places.
*/
WITH unique_locs AS (
    SELECT
        i.pid,
        i.tiv_2015,
        i.tiv_2016,
        count(*) OVER (
            PARTITION BY
                i.lat,
                i.lon
        ) AS unique_loc
    FROM
        insurance AS i
)

SELECT
    round(
        sum(ul.tiv_2016)::numeric,
        2
    ) AS tiv_2016
FROM
    unique_locs AS ul
WHERE
    ul.unique_loc = 1
    AND EXISTS (
        SELECT 1
        FROM
            unique_locs AS ul2
        WHERE
            ul.tiv_2015 = ul2.tiv_2015
            AND ul.pid != ul2.pid
    )
