-- READ UNCOMMITTED
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
-- go to session 2 and start the transaction

-- check for dirty reads
SELECT balance FROM accounts WHERE owner='alice';
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
SELECT balance FROM accounts WHERE owner='alice';
-- we can see uncommitted changes in this transaction, go to session 2 and check if we can see them in another transaction
ROLLBACK;


-- READ COMMITTED
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
-- go to session 2 and start the transaction

-- check for non-repeatable reads
SELECT balance FROM accounts WHERE owner='alice';
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
SELECT balance FROM accounts WHERE owner='alice';
-- go to session 2 and check if we can see uncommitted changes in another transaction
COMMIT;
-- go to session 2 and check if we can see committed changes in another transaction

-- check for phantom rows
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT * FROM accounts WHERE balance > 100.0;
INSERT INTO accounts(owner, balance) VALUES ('brian', 150.0);
SELECT * FROM accounts WHERE balance > 100.0;
-- go to session 2 and check if we can see uncommitted changes
COMMIT;


-- REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
-- go to session 2 and start the transaction
SELECT balance FROM accounts WHERE owner='alice';
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
SELECT balance FROM accounts WHERE owner='alice';
-- go to session 2 and check if we can see uncommitted changes in another transaction
COMMIT;
-- go to session 2 and check if we can see committed changes in another transaction

-- check for locks
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
-- go to session 2 and start the transaction
SELECT * FROM accounts WHERE balance > 100;
-- go to session 2 and insert new owner
SELECT * FROM accounts WHERE balance > 100;
-- we cannot see changes from session 2
COMMIT;
-- and can commit without errors or locks


-- SERIALIZABLE
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
-- go to session 2 and start transaction
SELECT * FROM accounts WHERE balance > 100;
-- go to session 2 and insert new owner
ROLLBACK;
