-- import sqlite3

-- Connect to SQLite3 database (creates if it doesn't exist)
-- conn = sqlite3.connect('database.db')
-- cursor = conn.cursor()

# Create Register table
cursor.execute(
    CREATE TABLE IF NOT EXISTS register (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
)

# Create Event table
cursor.execute(
    CREATE TABLE IF NOT EXISTS event (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        reg_no TEXT NOT NULL,
        gender TEXT NOT NULL,
        semester TEXT NOT NULL,
        event1 TEXT NOT NULL,
        event2 TEXT NOT NULL,
        event3 TEXT NOT NULL,
        register_id INTEGER,
        FOREIGN KEY (register_id) REFERENCES register(id)
    )
)

# Create EventDetails table
cursor.execute(
    CREATE TABLE IF NOT EXISTS eventdetails (
        id INTEGER PRIMARY KEY,
        tournament_name TEXT NOT NULL,
        sport_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        venue_date DATE NOT NULL,
        venue TEXT NOT NULL
    )
)

# Create ContactForm table
cursor.execute(
    CREATE TABLE IF NOT EXISTS contactform (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        mobile TEXT NOT NULL,
        message TEXT NOT NULL
    )
    )

# Create Result table
cursor.execute(
    CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY,
        sport_name TEXT NOT NULL,
        full_name TEXT NOT NULL,
        result TEXT NOT NULL,
        event_id INTEGER,
        FOREIGN KEY (event_id) REFERENCES event(id)
    )
)

# Commit changes and close the connection
conn.commit()
conn.close()