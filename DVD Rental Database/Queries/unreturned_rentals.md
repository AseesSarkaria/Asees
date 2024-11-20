```sql
SELECT 
	rental_id,
    rental_date,
    inventory_id,
    customer_id,
    return_date,
    staff_id,
    last_update
FROM rental
WHERE rental.return_date IS NULL
```
```text
---top 5 rows---
"rental_id"	"rental_date"	"inventory_id"	"customer_id"	"return_date"	"staff_id"	"last_update"
11496	"2006-02-14 15:16:03"	2047	155		1	"2006-02-16 02:30:53"
11541	"2006-02-14 15:16:03"	2026	335		1	"2006-02-16 02:30:53"
12101	"2006-02-14 15:16:03"	1556	479		1	"2006-02-16 02:30:53"
11563	"2006-02-14 15:16:03"	1545	83		1	"2006-02-16 02:30:53"
11577	"2006-02-14 15:16:03"	4106	219		2	"2006-02-16 02:30:53"
