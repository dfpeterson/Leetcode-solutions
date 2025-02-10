/*
Level: Medium
Link: https://leetcode.com/problems/tree-node/
Tags: database
Description:
Each node in the tree can be one of three types:
 * "Leaf": if the node is a leaf node.
 * "Root": if the node is the root of the tree.
 * "Inner": If the node is neither a leaf node nor a root node.

Write a solution to report the type of each node in the tree.

Return the result table in any order.
*/
SELECT
    t.id,
    CASE
        WHEN t.p_id IS null THEN 'Root'
        WHEN EXISTS (
            SELECT 1
            FROM
                tree AS n
            WHERE
                n.p_id = t.id
        ) THEN 'Inner'
        WHEN NOT EXISTS (
            SELECT 1
            FROM
                tree AS n
            WHERE
                n.p_id = t.id
        ) THEN 'Leaf'
    END AS type
FROM
    tree AS t
