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



