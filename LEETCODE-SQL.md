-- SQL LEET CODE Solutions: --

# 1667. Fix Names in a Table

```SQL
SELECT user_id,
CONCAT(
    UPPER(LEFT(name,1)),
    LOWER(RIGHT(name, (LENGTH(name)-1)))
) AS name
FROM Users
ORDER BY user_id;
```



# 1527. Patients With a Condition

```SQL
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions like '% DIAB1%' 
OR conditions like 'DIAB1%';
```

# 1484. Group Sold Products By The Date

```SQL
SELECT sell_date, count(distinct product) as num_sold, group_concat(distinct product) as products
FROM activities
GROUP BY sell_date;
```

# 1965. Employees With Missing Information

```SQL
SELECT employee_id 
FROM employees 
WHERE employee_id NOT IN (SELECT employee_id FROM salaries )
UNION
SELECT employee_id 
FROM salaries 
WHERE employee_id NOT IN (SELECT employee_id FROM employees)
ORDER BY employee_id;
```
# 1661. Average Time of Process per Machine

```SQL
WITH cte AS (
    SELECT a.machine_id, a.process_id, a.timestamp AS start_timestamp, 
           (SELECT b.timestamp FROM Activity b 
            WHERE b.activity_type = 'end' 
              AND b.machine_id = a.machine_id 
              AND b.process_id = a.process_id) AS end_timestamp
    FROM Activity a 
    WHERE a.activity_type = 'start'
)

SELECT machine_id, ROUND(AVG(end_timestamp - start_timestamp), 3) AS processing_time
FROM cte
GROUP BY machine_id
ORDER BY machine_id;

```
# 570. Managers with at Least 5 Direct Reports
```SQL
SELECT name
FROM (
    SELECT e1.name, count(e1.id) AS reportees FROM Employee e1
    JOIN Employee e2 
    WHERE e1.id = e2.managerId
    GROUP BY e2.managerId
) t1
WHERE reportees >= 5
```
# 
