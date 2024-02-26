import sqlite3

def create_table():
    # Connect to SQLite database (create if not exists)
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Define SQL command to create table
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        employeeNumber TEXT,
        clockInTime DATETIME,
        clockOutTime DATETIME,
        entryLatitude REAL,
        entryLongitude REAL,
        leavingLatitude REAL,
        leavingLongitude REAL,
        timeDuration TEXT
    );
    '''

    # Execute SQL command to create table
    cursor.execute(create_table_sql)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
