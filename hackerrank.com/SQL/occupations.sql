--https://www.hackerrank.com/challenges/occupations/problem

SELECT
    t1.Name,
    t2.Name,
    t3.Name,
    t4.Name
FROM
    (SELECT
        Name,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS id
    FROM
        OCCUPATIONS
    WHERE
        Occupation='Doctor') t1
FULL OUTER JOIN
    (SELECT
        Name,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS id
    FROM
        OCCUPATIONS
    WHERE
        Occupation='Professor') t2 ON t2.id=t1.id
FULL OUTER JOIN
    (SELECT
        Name,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS id
    FROM
        OCCUPATIONS
    WHERE
        Occupation='Singer') t3 ON t3.id=t2.id
FULL OUTER JOIN
    (SELECT
        Name,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS id
    FROM
        OCCUPATIONS
    WHERE
        Occupation='Actor') t4 ON t4.id=t3.id
