```sql
CREATE OR REPLACE FUNCTION update_summary_on_insert()
RETURNS TRIGGER AS $$
BEGIN
    TRUNCATE TABLE summary;
	
    INSERT INTO summary 
    SELECT 
        store_id,
        date_part('year', payment_date) AS year,
        date_part('month', payment_date) AS month,
        COUNT(*) AS purchase_volume,
        add_symbol( SUM(amount), '_m') AS revenue,
        add_symbol( MAX(amount), '_m') AS biggest_purchase,
        add_symbol( MIN(
            CASE
                WHEN (amount > 0) THEN amount
                ELSE NULL
            END), '_m') AS smallest_purchase,
        add_symbol( ROUND(AVG(amount), 2), '_m') AS average_purchase,
        CASE WHEN MAX(rental_duration) IS NULL
			THEN 'Month in progress - no returns yet'
			ELSE add_symbol( MAX(rental_duration), '_d')
		END AS longest_rental,
		CASE WHEN MIN(rental_duration) IS NULL
			THEN 'Month in progress - no returns yet'
			ELSE add_symbol( MIN(rental_duration), '_d')
		END AS shortest_rental,
		CASE WHEN MIN(rental_duration) IS NULL
			THEN 'Month in progress - no returns yet'
			ELSE add_symbol( round(AVG(rental_duration), 2), '_d')
		END AS average_rental
    FROM detailed
	WHERE payment_id IS NOT NULL
    GROUP BY store_id, date_part('year', payment_date), date_part('month', payment_date)
	ORDER BY 1, 2, 3 
	;
	RETURN NULL;
END;
$$ LANGUAGE plpgsql;
