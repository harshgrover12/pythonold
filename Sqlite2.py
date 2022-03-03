import sqlite3


conn = sqlite3.connect(':memory:')

cursr = conn.cursor()
cursr.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
)""")
cursr.execute("SELECT * FROM employees WHERE  last='Schafer'")
cursr.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
cursr.fetchone()  # Returns first row if exists else None
cursr.fetchmany(5)  # Returns 5 rows, else empty list
cursr.fetchall()  # Returns full table
# cursr.execute("INSERT INTO employees VALUES (?, ?, ?), (emp1.first, emp1.last, emp1.pay")
conn.commit()  # This commits the current transaction
conn.close()