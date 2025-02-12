```sql
CREATE OR REPLACE FUNCTION DATE_DIFF(start_date TIMESTAMP, end_date TIMESTAMP, unit TEXT DEFAULT NULL)
RETURNS numeric AS $$
BEGIN
    IF unit IS NULL THEN
        RETURN AGE(end_date, start_date)::TEXT;
    ELSE
        CASE unit
            WHEN 'day' THEN
                RETURN EXTRACT(DAY FROM (end_date - start_date))::TEXT;
            WHEN 'week' THEN
                RETURN (EXTRACT(DAY FROM (end_date - start_date)) / 7.0)::TEXT;
            WHEN 'month' THEN
                RETURN EXTRACT(MONTH FROM AGE(end_date, start_date))::TEXT;
            WHEN 'year' THEN
                RETURN EXTRACT(YEAR FROM AGE(end_date, start_date))::TEXT;
            ELSE
                RAISE EXCEPTION 'Invalid unit. Valid units are: day, week, month, year, or NULL.';
        END CASE;
    END IF;
END;
$$ LANGUAGE plpgsql;
