--Thread:10
INSERT INTO A_SCHEMA.A_TABLE(
    SELECT * FROM B_SCHEMA.B_TABLE
    WHERE 1 = 1
  );