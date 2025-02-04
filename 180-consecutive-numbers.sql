/*
Level: Medium
Link: https://leetcode.com/problems/consecutive-numbers/
Tags: database
Description:
Find all numbers that appear at least three times consecutively.

Return the result table in any order.
*/
with num_stack as (
    select
        l.num,
        lead(l.num) over (
            order by
                l.id
        ) as num2,
        lead(
            l.num,
            2)
            over (
                order by
                    l.id
            )
        as num3
    from
        logs as l
)

select num as consecutivenums
from
    num_stack
where
    num = num2
    and num = num3
group by
    num
