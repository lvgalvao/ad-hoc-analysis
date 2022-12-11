-- USING CTE

    SELECT SUM(CASE WHEN violation_id is null THEN 0 ELSE 1 END) as num_violations ,
        to_char(inspection_date:: date, 'YYYY') as year
    FROM sf_restaurant_health_violations
    WHERE business_name = 'Roxanne Cafe'
    GROUP BY year
    ORDER BY year ASC
