-- List records with a name in second_table by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
