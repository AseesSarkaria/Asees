```sql
SELECT 
	p.payment_id,
    p.customer_id,
    p.staff_id,
    p.rental_id,
    p.amount,
    p.payment_date
FROM payment p
 JOIN rental r ON (p.rental_id = r.rental_id)
WHERE r.rental_id IN (	SELECT payment.rental_id
           				FROM payment
          				GROUP BY payment.rental_id
         				HAVING count(payment.rental_id) > count(DISTINCT payment.rental_id)
					 )
```
```text
---Output--- 
"payment_id"	"customer_id"	"staff_id"	"rental_id"	"amount"	"payment_date"
19518	16	1	4591	1.99	"2007-02-18 03:24:38.996577"
25162	259	2	4591	1.99	"2007-03-23 04:41:42.996577"
29163	401	1	4591	0.99	"2007-04-12 04:54:36.996577"
31069	182	2	4591	3.99	"2007-04-08 04:58:09.996577"
31834	546	1	4591	3.99	"2007-04-30 19:44:46.996577"
