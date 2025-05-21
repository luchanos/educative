-- go to session 1 and setup the test table


-- READ UNCOMMITTED
-- go to session 1 and start the transaction
BEGIN TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE owner='alice';

-- check for dirty reads
-- go to session 1 and update alice`s balance
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see uncommitted changes from session 1 - dirty reads are not allowed in PostgreSQL and READ UNCOMMITTED behaves as READ COMMITTED
ROLLBACK;


-- READ COMMITTED
-- go to session 1 and start the transaction
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- check for non-repeatable reads
SELECT balance FROM accounts WHERE owner='alice';
-- go to session 1 and update alice`s balance
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see uncommitted changes from session 1 - dirty read is not possible in repeatable read transaction isolation level
-- go to session 1 and commit the update
SELECT balance FROM accounts WHERE owner='alice';
-- we cannot see committed changes from session 1 - non-repeatable read is not possible in repeatable read transaction isolation level. The same will be actual for phantom rows too.
COMMIT;

-- check for serialization errors
-- go to session 1 and start the transaction
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- go to session 1 and view bob`s balance
SELECT balance FROM accounts WHERE owner = 'alice';
-- go to session 1 and update alice`s balance
UPDATE accounts SET balance = balance - 10 WHERE owner = 'bob';
-- go to session 1 and commit
COMMIT;
-- we can commit without errors


-- SERIALIZABLE
-- go to session 1 and start the transaction
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- check for serialization errors
-- go to session 1 and view bob`s balance
SELECT balance FROM accounts WHERE owner = 'alice';
-- go to session 1 and update alice`s balance
UPDATE accounts SET balance = balance - 10 WHERE owner = 'bob';
-- go to session 1 and commit
COMMIT;
-- we got ERROR: could not serialize access

-- The SERIALIZABLE isolation level means that all transactions must behave
-- as if they were executed one after another, in a strict sequence. They don’t
-- actually run in order, but the final result must be consistent with some linear execution order.

-- session 1 -> session 2
-- session 1:
-- SELECT balance FROM accounts WHERE owner = 'bob'; -> bob`s balance = 50
-- UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice'; -> alice`s balance = 100 + 10 = 110
-- session 2:
-- SELECT balance FROM accounts WHERE owner = 'alice';
-- -> alice`s balance = 100 due to snapshot, but must be equal to 110 according to the update
-- in session 1 -> this will lead to serialization error during commit.


-- session 2 -> session 1
-- session 2:
-- SELECT balance FROM accounts WHERE owner = 'alice'; -> alice`s balance = 100
-- UPDATE accounts SET balance = balance - 10 WHERE owner = 'bob'; ->  bob`s balance = 50 - 10 = 40
-- session 1:
-- SELECT balance FROM accounts WHERE owner = 'bob';
-- -> bob`s balance = 50 due to snapshot, but must be equal to 40 according to the update
-- in session 2 -> this will lead to serialization error during commit.
