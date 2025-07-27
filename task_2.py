import sqlite3
import pandas as pd

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
    
    conn.commit()
    conn.close()

def get_customer_info(id):
    db_path = "customer.db"
    conn = None

    try:
        with sqlite3.connect(db_path) as conn:
            # Use parameterized query (?) to prevent SQL injection
            df = pd.read_sql_query("SELECT * FROM Customer WHERE id = ?", conn, params=(id,))
        return df
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return pd.DataFrame()
    
    finally:
        if conn:
            conn.close()

def get_customer_info_filter_date(id, start_date=None, end_date=None):
    db_path = "customer.db"
    conn = None
    
    try:
        with sqlite3.connect(db_path) as conn:
            if start_date and end_date:
                df = pd.read_sql_query("SELECT * FROM Customer WHERE id = ? AND created_at BETWEEN DATE ? AND DATE ?", conn, params=(id, start_date, end_date))
            else:
                # Use parameterized query (?) to prevent SQL injection
                df = pd.read_sql_query("SELECT * FROM Customer WHERE id = ?", conn, params=(id,))
        return df
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return pd.DataFrame()
    
    finally:
        if conn:
            conn.close()


