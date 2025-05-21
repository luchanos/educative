CREATE TABLE accounts(
	id serial,
	owner varchar(255) unique,
	balance float
);
INSERT INTO accounts (owner, balance) VALUES 
('alice', 100.0),
('bob', 50.0);
SELECT * FROM accounts;


-- READ UNCOMMITTED
BEGIN TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- go to session 2 and start the transaction

-- check for dirty reads
SELECT balance FROM accounts WHERE owner='alice';
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
SELECT balance FROM accounts WHERE owner='alice';
-- we can see uncommitted changes in this transaction, go to session 2 and check if we can see them in another transaction
ROLLBACK;


-- READ COMMITTED
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- go to session 2 and start the transaction

-- check for non-repeatable reads
SELECT balance FROM accounts WHERE owner='alice';
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
SELECT balance FROM accounts WHERE owner='alice';
-- go to session 2 and check if we can see uncommitted changes in another transaction
COMMIT;
-- go to session 2 and check if we can see committed changes in another transaction

-- check for serialization errors
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- go to session 2 and start the transaction
SELECT balance FROM accounts WHERE owner = 'bob';
-- go to session 2 and view alice`s balance
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
-- go to session 2 and update bob`s balance
COMMIT;
-- go to session 2 and commit


-- SERIALIZABLE
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- go to session 2 and start transaction

-- check for serialization errors
SELECT balance FROM accounts WHERE owner = 'bob';
-- go to session 2 and view alice`s balance
UPDATE accounts SET balance = balance + 10 WHERE owner = 'alice';
-- go to session 2 and update bob`s balance
COMMIT;
-- go to session 2 and commit
