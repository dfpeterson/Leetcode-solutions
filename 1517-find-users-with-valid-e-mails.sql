/*
Level: Easy
Link: https://leetcode.com/problems/find-users-with-valid-e-mails/
Tags: database
Description:
Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

    The prefix name is a string that may contain letters (upper or lower case),
digits, underscore '_', period '.', and/or dash '-'. The prefix name must start
with a letter.
 * The domain is '@leetcode.com'.

Return the result table in any order.
*/
SELECT
    u.user_id,
    u.name,
    u.mail
FROM
    users AS u
WHERE
    lower(u.mail) SIMILAR TO '[a-z][a-z0-9\-\.\_]*@leetcode\.com'
