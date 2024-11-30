```sql
CREATE OR REPLACE PROCEDURE refresh_summary()
LANGUAGE plpgsql
AS $$
BEGIN

    CREATE TABLE IF NOT EXISTS detailed (
        payment_id INTEGER,
        return_date TIMESTAMP WITHOUT TIME ZONE,
        inventory_id INTEGER,
        store_id SMALLINT,
        rental_date TIMESTAMP WITHOUT TIME ZONE,
        customer_name TEXT,
        rental_duration TEXT,
        sales_rep TEXT
    );

    CREATE TABLE IF NOT EXISTS summary (
        store_id,
        year,
        month,
        purchase_volume,
        revenue,
        mom_purchase_volume,
        mom_revenue,
        mom_purchases_to_revenue_ratio,
        biggest_purchase,
        smallest_purchase,
        max_min_difference,
        average_purchase,
        median_purchase,
        avg_med_difference,
        standard_deviation
    )

    TRUNCATE TABLE detailed;
    TRUNCATE TABLE summary;

    INSERT INTO detailed 
	SELECT 
        p.payment_id, 
        c.first_name || ' ' || c.last_name AS customer_name, 
        r.rental_date, 
        r.return_date, 
    	ADD_SYMBOL(DATE_DIFF(r.rental_date, r.return_date, 'DAY'), '_d')  AS rental_duration, 
    	r.inventory_id,  
        s.first_name || ' ' || s.last_name AS sales_rep, 
    	s.store_id 
    FROM rental r 
    JOIN customer c USING (customer_id) 
    JOIN staff s USING (staff_id) 
    LEFT JOIN payment p USING (rental_id)  
    ORDER BY r.rental_date ASC 

    INSERT INTO summary
    SELECT 
        b.store_id,
        date_part('year', a.rental_date) AS year,
        date_part('month', a.rental_date) AS month,
        COUNT(*) AS purchase_volume,
        SUM(a.payment_id) AS revenue, -- Replace payment_id with actual revenue field
        NULL AS mom_purchase_volume, -- Placeholder for MoM calculations
        NULL AS mom_revenue,         -- Placeholder for MoM calculations
        NULL AS mom_purchases_to_revenue_ratio, -- Placeholder for MoM calculations
        MAX(a.payment_id) AS biggest_purchase, -- Replace with actual amount field
        MIN(
            CASE
                WHEN (a.payment_id > 0) THEN a.payment_id
                ELSE NULL
            END) AS smallest_purchase,
        MAX(a.payment_id) - MIN(
            CASE
                WHEN (a.payment_id > 0) THEN a.payment_id
                ELSE NULL
            END) AS max_min_difference,
        ROUND(AVG(a.payment_id), 2) AS average_purchase, -- Replace as needed
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY a.payment_id) AS median_purchase, -- Replace as needed
        ROUND(AVG(a.payment_id), 2) - PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY a.payment_id) AS avg_med_difference, -- Replace as needed
        ROUND(STDDEV(a.payment_id), 2) AS standard_deviation -- Replace as needed
    FROM detailed a
    JOIN staff b ON a.inventory_id = b.staff_id
    GROUP BY b.store_id, date_part('year', a.rental_date), date_part('month', a.rental_date);
END;
$$;