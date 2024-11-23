```sql
SELECT
    p.payment_id,
    c.first_name || ' ' || c.last_name 
		AS customer_name,
    r.rental_date,
    r.return_date,
	ADD_SYMBOL(DATE_DIFF(r.rental_date, r.return_date, 'DAY'), '_d') 
		AS rental_duration,
	r.inventory_id, 
    s.first_name || ' ' || s.last_name 
		AS sales_rep,
	s.store_id
FROM rental r
 JOIN customer c USING (customer_id)
 JOIN staff s USING (staff_id)
 LEFT JOIN payment p USING (rental_id) 
ORDER BY r.rental_date ASC
```
```table
| "payment_id"       | "customer_name"       | "rental_date"         | "return_date" | "rental_duration" | "inventory_id" | "sales_rep" | "store_id" |
|--------------------|-----------------------|-----------------------|---------------|-------------------|----------------|-------------|------------|
| "Charlotte Hunter" | "2005-05-24 22:53:30" | "2005-05-26 22:04:30" | "1 days"      | 367               | "Mike Hillyer" | 1           |            |
| "Tommy Collazo"    | "2005-05-24 22:54:33" | "2005-05-28 19:40:33" | "3 days"      | 1525              | "Mike Hillyer" | 1           |            |
| "Manuel Murrell"   | "2005-05-24 23:03:39" | "2005-06-01 22:12:39" | "7 days"      | 1711              | "Mike Hillyer" | 1           |            |
| "Andrew Purdy"     | "2005-05-24 23:04:41" | "2005-06-03 01:43:41" | "9 days"      | 2452              | "Jon Stephens" | 2           |            |
| "Delores Hansen"   | "2005-05-24 23:05:21" | "2005-06-02 04:33:21" | "8 days"      | 2079              | "Mike Hillyer" | 1           |            |
