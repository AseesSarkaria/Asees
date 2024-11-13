```sql
SELECT 
	i.film_id,
	count(*) AS count
FROM unreturned_rentals r
 JOIN inventory i USING (inventory_id)
GROUP BY i.film_id
```
```text
---top 5 rows---
"film_id"	"count"
270	        1
496	        1
625	        1
228        	1
667	        1
