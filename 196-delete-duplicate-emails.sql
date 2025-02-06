/*
Level: Easy
Link: https://leetcode.com/problems/delete-duplicate-emails/
Tags: database
Description:
Write a solution to delete all duplicate emails, keeping only one unique email
with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement
and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver
will first compile and run your piece of code and then show the Person table.
The final order of the Person table does not matter.
*/
WITH extra_emails AS (
    SELECT
        p.id,
        row_number() OVER (
            PARTITION BY p.email
            ORDER BY
                p.id
        ) AS the_row
    FROM
        person AS p
)

DELETE
FROM
person p
USING extra_emails e
WHERE
    e.id = p.id
    AND e.the_row > 1
