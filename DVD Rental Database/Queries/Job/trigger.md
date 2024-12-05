```sql
CREATE TRIGGER update_summary_after_insert
AFTER INSERT ON detailed
FOR EACH STATEMENT --- STATEMENT because aggreagates should be computed in one pass, not recomputed for each row changed in a recursive fasion; otherwise, time time to load the inital data into the Detailed table would be 100x more than necessary 
EXECUTE FUNCTION update_summary_on_insert();
