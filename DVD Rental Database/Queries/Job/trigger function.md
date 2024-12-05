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
        SUM(amount) AS revenue,
        MAX(amount) AS biggest_purchase,
        MIN(
            CASE
                WHEN (amount > 0) THEN amount
                ELSE NULL
            END) AS smallest_purchase,
        ROUND(AVG(amount), 2) AS average_purchase,
        MAX(rental_duration) AS longest_rental,
		MIN(rental_duration) AS shortest_rental,
		round(AVG(rental_duration), 2) AS average_rental
    FROM detailed
	WHERE payment_id IS NOT NULL
    GROUP BY store_id, date_part('year', payment_date), date_part('month', payment_date)
	ORDER BY 1, 2, 3 
	;
	RETURN NULL;
END;
$$ LANGUAGE plpgsql;
