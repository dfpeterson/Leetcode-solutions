/*
Level: Easy
Link: https://leetcode.com/problems/average-time-of-process-per-machine/
Tags: database
Description:
There is a factory website that has several machines each running the same
number of processes. Write a solution to find the average time each machine
takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start'
timestamp. The average time is calculated by the total time to complete every
process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as
processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.
*/
SELECT
    a.machine_id,
    round(
        avg(b.timestamp - a.timestamp)::NUMERIC,
        3
    ) AS processing_time
FROM
    activity AS a
INNER JOIN activity AS b
    ON
        a.machine_id = b.machine_id
        AND a.process_id = b.process_id
        AND b.activity_type = 'end'
WHERE
    a.activity_type = 'start'
GROUP BY
    a.machine_id
