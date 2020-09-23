--https://www.hackerrank.com/challenges/binary-search-tree-1/problem

--1
SELECT
    b1.N,
    CASE
        WHEN b1.P IS NULL THEN 'Root'
        WHEN COUNT(*) = 2 THEN 'Inner'
        ELSE 'Leaf'
    END
FROM
    BST b1
LEFT JOIN
    BST b2 ON b2.P=b1.N
GROUP BY
    b1.N,
    b1.P
ORDER BY
    b1.N

--2
SELECT
    b1.N,
    IF(b1.P IS NULL, 'Root', IF((SELECT COUNT(*) FROM BST b2 WHERE b2.P=b1.N)>0, 'Inner', 'Leaf'))
FROM
    BST b1
ORDER BY
    b1.N

--3
SELECT
    b.N,
    CASE
        WHEN b.P IS NULL THEN 'Root'
        WHEN b.N IN (SELECT b.P FROM BST b) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM
    BST b
ORDER BY
    b.N;