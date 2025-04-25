import sqlite3

CONN = sqlite3.connect('departments.db')  # or 'department.db' if persistence is required
CURSOR = CONN.cursor()
