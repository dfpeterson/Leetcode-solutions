/*
Level: Medium
Link: https://leetcode.com/problems/game-play-analysis-iv/
Tags: database
Description:
Write a solution to report the fraction of players that logged in again on the
day after the day they first logged in, rounded to 2 decimal places. In other
words, you need to count the number of players that logged in for at least two
consecutive days starting from their first login date, then divide that number
by the total number of players.
*/
WITH consecutive_days AS (
    SELECT
        a.player_id,
        CASE
            WHEN
                a.event_date + interval '1 day'
                = coalesce(lead(a.event_date) OVER (
                    PARTITION BY a.player_id
                    ORDER BY
                        a.event_date
                ),
                a.event_date + interval '1 day')
                AND
                coalesce(lead(a.games_played) OVER (
                    PARTITION BY a.player_id
                    ORDER BY
                        a.event_date
                ),
                0) >= 1 THEN 1
            ELSE 0
        END AS consecutive_play,
        row_number() OVER (
            PARTITION BY a.player_id
            ORDER BY
                a.event_date
        ) AS day_order
    FROM
        activity AS a
)

SELECT
    round(
        avg(cd.consecutive_play)::numeric,
        2
    ) AS fraction
FROM
    consecutive_days AS cd
WHERE
    cd.day_order = 1
