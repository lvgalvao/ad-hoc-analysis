-- TO CALCULATE THE GROUWTH WE'll USE THE WINDOW FUNCTION LAG,
-- THIS WINDOW FUNCTION RETURN THE VALUES OF A ROW "BEFORE"

WITH cte_year_host AS (
SELECT  *,
        extract(year from host_since) as year_host
FROM airbnb_search_details
),

cte_qte_host_by_year AS (
SELECT year_host, COUNT(id) as qte_host_by_year
FROM cte_year_host
GROUP BY year_host
ORDER BY year_host asc),

cte_last_year_qte_host AS (
SELECT  year_host, 
        qte_host_by_year,
        lag(qte_host_by_year, 1) over(order by year_host asc) as last_year_qte_host
from cte_qte_host_by_year)

SELECT *, round(((qte_host_by_year-last_year_qte_host)/(last_year_qte_host::numeric))*100,0) as growth
FROM cte_last_year_qte_host