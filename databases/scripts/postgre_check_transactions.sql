-- PostgreSQL includes a view (also known as a virtual table) called pg_stat_activity.
-- It provides information about active sessions in the database at the current moment.
-- A detailed description of the columns is available here:
-- https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW.
--
-- In the context of identifying open transactions, the columns `state`, `query`, and `backend_xid`
-- may be of particular interest.
--
-- The state column indicates the current state of the session:
-- `active`: a command is currently being executed
-- `idle`: waiting for a command from the client
-- `idle in transaction`: a transaction is open, but no command is currently being executed
-- `idle` in transaction (aborted)`: similar to idle in transaction, but one of the previous commands caused an error.
-- 
-- The `query` column contains the text of the currently executing query when state = 'active',
-- or the last executed query for other states.
-- 
-- Each transaction is assigned an ID (XID). The `backend_xid` column contains this XID.
-- 
-- A query to display all open (unclosed) transactions:

SELECT * FROM pg_stat_activity WHERE state LIKE 'idle in transaction%';

-- Also each table in PostgreSQL has internal (system) columns.
-- In the context of transactions, the following are of particular interest:
-- `xmin` (type xid) — the ID of the transaction that created the row.
-- `xmax` (type xid) — the ID of the transaction that deleted or updated the row. If the row is still "alive", then xmax = 0.
-- Example: within a transaction, you can do the following and see XID of transaction in `xmin` column:

INSERT INTO accounts (owner, balance) VALUES ('charlie', 150.0);

SELECT xmin::text, xmax::text, * FROM accounts WHERE owner = 'charlie';
