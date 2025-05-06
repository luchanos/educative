insert into users (name, surname, unique_code) values ('Ivan', 'Petrov', 'a');


BEGIN;
INSERT INTO users (name, surname, unique_code) VALUES ('Alice', 'Smith', 'code123');
UPDATE users SET surname = 'Johnson' WHERE name = 'Alice';
COMMIT;

BEGIN;
INSERT INTO users (name, surname, unique_code) VALUES ('Bob', 'Miller', 'code125');  -- OK
INSERT INTO users (name, surname, unique_code) VALUES ('John', 'Doe', 'code125');   -- ❌ duplicate key
ROLLBACK;  -- Because the 2nd insert fails

BEGIN;

BEGIN;
SAVEPOINT my_savepoint;
-- risky operation
INSERT INTO users (name, surname, unique_code) VALUES ('Oops', 'Dupe', 'code001');
-- if error:
ROLLBACK TO my_savepoint;
-- continue with other stuff...
COMMIT;

select * from users;

rollback;

DO $$
BEGIN
  BEGIN
    INSERT INTO users (name, surname, unique_code) VALUES ('test', 'rollback', '123abc');
  EXCEPTION WHEN unique_violation THEN
    RAISE NOTICE 'Duplicate code!';
  END;
END;
$$;

SELECT
    pid,
    usename,
    datname,
    state,
    backend_start,
    xact_start,
    query_start,
    state_change,
    query
FROM
    pg_stat_activity
WHERE
    xact_start IS NOT NULL
ORDER BY
    xact_start;


SELECT
  pid,
  usename,
  state,
  backend_xid,
  xact_start,
  query
FROM pg_stat_activity
WHERE state = 'active' AND xact_start IS NOT NULL;