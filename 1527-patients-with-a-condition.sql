/*
Level: Easy
Link: https://leetcode.com/problems/patients-with-a-condition/
Tags: database
Description:
Write a solution to find the patient_id, patient_name, and conditions of the
patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1
prefix.

Return the result table in any order.
*/
SELECT
    p.patient_id,
    p.patient_name,
    p.conditions
FROM
    patients AS p
WHERE
    p.conditions ILIKE '% diab1%'
    OR p.conditions ILIKE 'diab1%'
