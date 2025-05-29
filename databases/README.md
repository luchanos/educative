# Transaction isolation levels – SQL & Python examples

This project demonstrates how different transaction isolation levels behave in relational databases using Python and SQL scripts.

## Start databases with Docker
Both PostgreSQL and MySQL are required. You can spin them up using Docker:

```bash
docker-compose -f ./databases/docker-compose.yaml up -d
```

PostgreSQL will be available at `localhost:5432`. MySQL will be available at `localhost:3306`. Make sure ports are free and Docker is running.

## Setup for Python examples
1. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Try the examples

### Jupyter Notebook

Open the notebook [transaction_isolation_levels.ipynb](./transaction_isolation_levels.ipynb).

`READ UNCOMMITTED` is demonstrated with MySQL (since PostgreSQL doesn't support dirty reads). All other levels are shown using PostgreSQL.

### SQL Scripts

Inside the `scripts/` folder:

    mysql_session1.sql, mysql_session2.sql     — MySQL examples for all isolation levels
    postgre_session1.sql, postgre_session2.sql — PostgreSQL examples
    postgre_check_transactions.sql             — Shows open transactions via pg_stat_activity

Run paired scripts in two terminal sessions (Session 1 and Session 2) using your preferred SQL client.
