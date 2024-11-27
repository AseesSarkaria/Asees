CREATE OR REPLACE PROCEDURE refresh_summary()
LANGUAGE plpgsql
AS $$
BEGIN
    -- Clear the contents of the detailed and summary tables
    TRUNCATE TABLE detailed;
    TRUNCATE TABLE summary;

    -- Recreate the detailed table
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

    -- Populate the summary table
    INSERT INTO summary (
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
