```sql
CREATE OR REPLACE FUNCTION infer_symbol_by_column(value ANYELEMENT, column_name TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN CASE 
        WHEN column_name LIKE '%_p' THEN CONCAT(value::TEXT, '%')
        WHEN column_name LIKE '%_m' THEN CONCAT('$', value::TEXT)
        -- other cases
        ELSE value::TEXT
    END;
END;
$$ LANGUAGE plpgsql;
