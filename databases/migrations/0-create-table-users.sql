CREATE TABLE accounts(
	id serial,
	owner varchar(255) unique,
	balance float
);

INSERT INTO accounts (owner, balance) VALUES ('alice', 100.0), ('bob', 50.0);
