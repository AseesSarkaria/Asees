```sql
SELECT 
	f.film_id,
	f.count AS total_owned,
	(f.count - COALESCE(i.count, 0) AS in_inventory,
	COALESCE(i.count, 0) AS rented_out
FROM films_in_inventory f
 LEFT JOIN current_inventory_out i USING (film_id)
```
```text
--top 5 rows---
"film_id"  "total_owned"  "in_inventory"  "rented_out"
652	        4	         4	         0
273	        7	         6	         1
51	        6            	 6	         0
951        	7	         7	         0
839	        2                2	         0
