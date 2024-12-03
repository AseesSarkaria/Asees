```sql
CREATE TABLE summary (
    store_id INTEGER, 
    year DOUBLE PRECISION, 
    month DOUBLE PRECISION, 
    purchase_volume BIGINT, 
    revenue NUMERIC, 
    mom_purchase_volume NUMERIC, 
    mom_revenue NUMERIC, 
    mom_purchases_to_revenue_ratio NUMERIC, 
    biggest_purchase NUMERIC, 
    smallest_purchase NUMERIC, 
    max_min_difference NUMERIC, 
    average_purchase NUMERIC, 
    median_purchase DOUBLE PRECISION, 
    avg_med_difference DOUBLE PRECISION, 
    standard_deviation NUMERIC 
);
```
```sql
CREATE TABLE IF NOT EXISTS summary (
        store_id INTEGER, 
        year DOUBLE PRECISION, 
        month DOUBLE PRECISION, 
        purchase_volume INT, 
        revenue NUMERIC, 
        biggest_purchase NUMERIC, 
        smallest_purchase NUMERIC, 
	longest_rental NUMERIC,
	shortest_rental NUMERIC,
	average_rental_duration NUMERIC
    )
