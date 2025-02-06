/*
Level: Hard
Link: https://leetcode.com/problems/first-letter-capitalization-ii/
Tags: database
Description:
Write a solution to transform the text in the content_text column by applying
the following rules:
 * Convert the first letter of each word to uppercase and the remaining
   letters to lowercase
 * Special handling for words containing special characters:
   * For words connected with a hyphen -, both parts should be capitalized
     (e.g., top-rated → Top-Rated)
   * All other formatting and spacing should remain unchanged

Return the result table that includes both the original content_text and the
modified text following the above rules.
*/
WITH array_split AS (
    SELECT
        uc.content_id,
        uc.content_text AS original_text,
        string_to_table(
            lower(uc.content_text),
            null
        ) AS array_text
    FROM
        user_content AS uc
),

fixed_characters AS (
    SELECT
        content_id,
        original_text,
        CASE
            WHEN
                array_text = '-'
                AND lag(array_text) OVER (PARTITION BY content_id) IS null
                THEN '--'
            WHEN
                coalesce(
                    lag(array_text) OVER (PARTITION BY content_id),
                    ' '
                ) IN (' ', '-'
                )
                THEN upper(array_text)
            ELSE
                array_text
        END
        AS fixed
    FROM
        array_split
)

SELECT
    content_id,
    original_text,
    string_agg(
        fixed,
        ''
    ) AS converted_text
FROM
    fixed_characters
GROUP BY
    content_id,
    original_text
