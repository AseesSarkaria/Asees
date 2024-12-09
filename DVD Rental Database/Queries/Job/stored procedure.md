```sql
CREATE OR REPLACE PROCEDURE refresh_summary()
LANGUAGE plpgsql
AS $$
BEGIN

    CREATE TABLE IF NOT EXISTS detailed (
	customer_name		text
	,amount			numeric
	,payment_date		timestamp without time zone
	,rental_date		timestamp without time zone
	,return_date		timestamp without time zone
	,rental_duration	numeric
	,sales_rep		text
	,store_id		smallint
	,payment_id		integer
	,inventory_id		integer
	);

	CREATE TABLE IF NOT EXISTS summary (
		store_id 		INTEGER, 
		year 			DOUBLE PRECISION, 
		month 			DOUBLE PRECISION, 
		purchase_volume 	INT, 
		revenue 		TEXT, 
		biggest_purchase 	TEXT, 
		smallest_purchase 	TEXT, 
		avgerage_purchase 	TEXT,
		longest_rental		TEXT,
		shortest_rental 	TEXT,
		average_rental 		TEXT
	);


    TRUNCATE TABLE detailed;
    TRUNCATE TABLE summary;

	INSERT INTO detailed 
	SELECT 
		c.first_name || ' ' || c.last_name AS customer_name, 
		p.amount,
		p.payment_date,
		r.rental_date, 
		r.return_date, 
		DATE_DIFF(r.rental_date, r.return_date, 'day') AS rental_duration, 
		s.first_name || ' ' || s.last_name AS sales_rep,
		s.store_id,
		p.payment_id, 
		r.inventory_id
	FROM rental r 
	JOIN customer c USING (customer_id) 
	JOIN staff s USING (staff_id) 
	LEFT JOIN payment p USING (rental_id)  
	ORDER BY r.rental_date ASC
	;

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

END;
$$;

