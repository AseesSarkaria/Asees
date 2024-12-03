```sql
CREATE TABLE IF NOT EXISTS detailed (
	customer_name	text
	,amount			numeric
	,payment_date		timestamp without time zone
	,rental_date		timestamp without time zone
	,return_date		timestamp without time zone
	,rental_duration	numeric
	,sales_rep		text
	,store_id		smallint
	,payment_id		integer
	,inventory_id		integer
)
