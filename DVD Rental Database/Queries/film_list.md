SELECT 
	inventory.film_id,
  count(*) AS count
FROM inventory
GROUP BY inventory.film_id

---top 5 rows---
"film_id"	"count"
652	      4
273	      7
51	      6
951	      7
839	      2
