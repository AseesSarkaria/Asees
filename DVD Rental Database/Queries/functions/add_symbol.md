```sql
CREATE OR REPLACE FUNCTION add_symbol(value ANYELEMENT, column_name TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN CASE 
        WHEN column_name LIKE '%_p' THEN CONCAT(value::TEXT, '%')
        WHEN column_name LIKE '%_m' THEN CONCAT('$', value::TEXT)

        ELSE value::TEXT
    END;
END;
$$ LANGUAGE plpgsql;
