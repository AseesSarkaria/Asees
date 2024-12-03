```sql
CREATE OR REPLACE FUNCTION update_summary_on_insert()
RETURNS TRIGGER AS $$
BEGIN
    -- Insert or update the summary table
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
        NEW.store_id,
        date_part('year', NEW.rental_date) AS year,
        date_part('month', NEW.rental_date) AS month,
        COUNT(*) AS purchase_volume,
        SUM(NEW.payment_id) AS revenue, -- Replace with actual revenue field
        NULL AS mom_purchase_volume, -- Placeholder for Month-over-Month calculations
        NULL AS mom_revenue,         -- Placeholder for Month-over-Month calculations
        NULL AS mom_purchases_to_revenue_ratio, -- Placeholder for Month-over-Month calculations
        MAX(NEW.payment_id) AS biggest_purchase, -- Replace with actual amount field
        MIN(
            CASE
                WHEN (NEW.payment_id > 0) THEN NEW.payment_id
                ELSE NULL
            END) AS smallest_purchase,
        MAX(NEW.payment_id) - MIN(
            CASE
                WHEN (NEW.payment_id > 0) THEN NEW.payment_id
                ELSE NULL
            END) AS max_min_difference,
        ROUND(AVG(NEW.payment_id), 2) AS average_purchase,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY NEW.payment_id) AS median_purchase,
        ROUND(AVG(NEW.payment_id), 2) - PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY NEW.payment_id) AS avg_med_difference,
        ROUND(STDDEV(NEW.payment_id), 2) AS standard_deviation
    FROM detailed
    GROUP BY store_id, date_part('year', NEW.rental_date), date_part('month', NEW.rental_date)


    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
```sql
CREATE OR REPLACE FUNCTION update_summary_on_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO summary 
    SELECT 
        NEW.store_id,
        date_part('year', NEW.payment_date) AS year,
        date_part('month', NEW.payment_date) AS month,
        COUNT(*) AS purchase_volume,
        add_symbol(SUM(NEW.amount), '_m') AS revenue,
        add_symbol(MAX(NEW.amount), '_m') AS biggest_purchase,
        add_symbol(MIN(
            CASE
                WHEN (NEW.amount > 0) THEN NEW.amount
                ELSE NULL
            END), '_m') AS smallest_purchase,
        add_symbol(ROUND(AVG(NEW.amount), 2), '_m') AS average_purchase,
        add_symbol(MAX(NEW.rental_duration), '_d') AS longest_rental,
		add_symbol(MIN(NEW.rental_duration), '_d') AS shortest_rental,
		add_symbol(round(AVG(NEW.rental_duration), 2), '_d') AS average_rental
    FROM detailed
	WHERE NEW.payment_id IS NOT NULL
    GROUP BY store_id, date_part('year', NEW.payment_date), date_part('month', NEW.payment_date)
	;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
