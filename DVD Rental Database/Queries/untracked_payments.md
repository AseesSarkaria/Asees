SELECT 
	r.rental_id,
    r.rental_date,
    r.inventory_id,
    r.customer_id,
    r.return_date,
    r.staff_id,
    r.last_update
FROM rental r
 LEFT JOIN payment p USING (rental_id)
WHERE p.payment_id IS NULL 
  AND r.return_date IS NOT NULL

---top 5 rows---
"rental_id"	"rental_date"	"inventory_id"	"customer_id"	"return_date"	"staff_id"	"last_update"
251	"2005-05-26 14:35:40"	4352	204	"2005-05-29 17:17:40"	1	"2006-02-16 02:30:53"
2024	"2005-06-17 13:00:51"	2566	329	"2005-06-22 07:03:51"	1	"2006-02-16 02:30:53"
1101	"2005-05-31 14:13:59"	1174	260	"2005-06-07 15:49:59"	1	"2006-02-16 02:30:53"
599	"2005-05-28 14:05:57"	4136	393	"2005-06-01 16:41:57"	2	"2006-02-16 02:30:53"
359	"2005-05-27 06:48:33"	1156	152	"2005-05-29 03:55:33"	1	"2006-02-16 02:30:53"
