-- HR ATTRITION PROJECT - Cerlin - Final SQL File
USE hr_attrition;

-- 1. Total Employees and Attrition Count
SELECT COUNT(*) AS Total_Employees FROM cleaned_hr_data;
SELECT COUNT(*) AS Left_Company FROM cleaned_hr_data WHERE Attrition='Yes';

-- 2. Overtime Analysis (Main Reason 2)
SELECT OverTime, 
COUNT(*) AS Total,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_Count
FROM cleaned_hr_data GROUP BY OverTime;

-- 3. Department Wise Attrition
SELECT Department, COUNT(*) AS Total, SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_Count FROM cleaned_hr_data GROUP BY Department;

-- 4. Salary Wise Analysis (Main Reason 1)
SELECT 
CASE 
 WHEN MonthlyIncome < 3000 THEN 'Low Salary'
 WHEN MonthlyIncome < 6000 THEN 'Medium Salary'
 ELSE 'High Salary'
END AS Salary_Group,
COUNT(*) AS Total,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_Count
FROM cleaned_hr_data GROUP BY Salary_Group;