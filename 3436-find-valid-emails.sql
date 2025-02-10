/*
Level: Easy
Link: https://leetcode.com/problems/find-valid-email-addresses/
Tags: database
Description:
Write a solution to find all the valid email addresses. A valid email address
meets the following criteria:
 * It contains exactly one @ symbol.
 * It ends with .com.
 * The part before the @ symbol contains only alphanumeric characters and
   underscores.
 * The part after the @ symbol and before .com contains a domain name that
   contains only letters.
Return the result table ordered by user_id in ascending order.
*/
SELECT
    u.user_id,
    u.email
FROM
    users AS u
WHERE
    u.email SIMILAR TO '[0-9A-Za-z_]+@[A-Za-z]+\.[Cc][Oo][Mm]'
