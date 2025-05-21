-- go to session 1 and setup the test table


-- READ UNCOMMITTED
-- go to session 1 and start the transaction
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
SELECT balance FROM accounts WHERE owner='alice';

-- check for dirty reads
-- go to session 1 and update alice`s balance
SELECT balance FROM accounts WHERE owner='alice';
-- we can see uncommitted changes from session 1 - dirty read
ROLLBACK;


-- READ COMMITTED
-- go to session 1 and start the transaction
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT balance FROM accounts WHERE owner='alice';

-- check for non-repeatable reads
-- go to session 1 and update alice`s balance
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see uncommitted changes from session 1 - dirty read is not possible in read committed transaction isolation level
-- go to session 1 and commit the update
SELECT balance FROM accounts WHERE owner='alice';
-- now we can see committed changes from session 1 - non-repeatable read
-- non-repeatable read occurs when a transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read)

-- check for phantom rows
SELECT * FROM accounts WHERE balance > 100.0;
-- go to session 1, start new transaction and add new rows
SELECT * FROM accounts WHERE balance > 100.0;
-- we still cannot see uncommitted changes from session 1
-- go to session 1 and commit the update
SELECT * FROM accounts WHERE balance > 100.0;
-- now we can see committed changes from session 1 - phantom rows
-- phantom rows occurs when a transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.
COMMIT;


-- REPEATABLE READ
-- go to session 1 and start the transaction
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;

-- check for non-repeatable reads
SELECT balance FROM accounts WHERE owner='alice';
-- go to session 1 and update alice`s balance
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see uncommitted changes from session 1 - dirty read is not possible in repeatable read transaction isolation level
-- go to session 1 and commit the update
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see committed changes from session 1 - non-repeatable read is not possible in repeatable read transaction isolation level. The same will be actual for phantom rows too.
COMMIT;

-- check for locks
-- go to session 1 and start the transaction
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
-- go to session 1 and view owners with balance > 100
INSERT INTO accounts (owner, balance) VALUES ('carol', 110.0);
COMMIT;
-- go to session 1, view owners with balance > 100 and commit


-- SERIALIZABLE
-- go to session 1 and start transaction
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
-- go to session 1 and view owners with balance > 100
INSERT INTO accounts (owner, balance) VALUES ('caroline', 170.0);
-- we got a lock!
ROLLBACK;
