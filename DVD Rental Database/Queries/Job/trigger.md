```sql
CREATE TRIGGER update_summary_after_insert
AFTER INSERT ON detailed
FOR EACH STATEMENT
EXECUTE FUNCTION update_summary_on_insert();
