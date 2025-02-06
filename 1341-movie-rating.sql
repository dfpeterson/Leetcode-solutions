/*
Level: Medium
Link: https://leetcode.com/problems/movie-rating/
Tags: database
Description:
Write a solution to:
 * Find the name of the user who has rated the greatest number of movies. In
   case of a tie, return the lexicographically smaller user name.
 * Find the movie name with the highest average rating in February 2020. In
   case of a tie, return the lexicographically smaller movie name.
*/
(
    SELECT u.name AS results
    FROM
        movierating AS mr
    INNER JOIN users AS u
        ON
            mr.user_id = u.user_id
    GROUP BY
        u.name
    ORDER BY
        count(mr.movie_id) DESC,
        u.name
    LIMIT 1
)
UNION ALL
(
    SELECT m.title
    FROM
        movierating AS mr
    INNER JOIN movies AS m
        ON
            mr.movie_id = m.movie_id
    WHERE
        mr.created_at BETWEEN '2020-02-01' AND '2020-02-28'
    GROUP BY
        m.title
    ORDER BY
        avg(mr.rating) DESC,
        m.title
    LIMIT 1
)
