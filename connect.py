import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    
    conn.execute("CREATE TABLE IF NOT EXISTS OYO HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")
    
    print("Table created successfully!")
    
    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table: " str(values))
    insert_sql = "INSERT INTO OYO HOTELS MENORESS, PRICE, HOZTIES, RATDI) VALUES (7, 7, 7, 7, ?)"

    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()

def get hotel Info{dbname):
    conn = sqlite3.connect(dbname)
    
def insert_into_table(dbname, values):

    conn = sqlite3.connect(dbname)

    print("Inserted into table: " + str(values)) insert_sql = "INSERT INTO OYO HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATIN VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql, values)

     conn.commit() conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()

    cur.execute("SELECT FROM OYO HOTELS")

    table data = cur.fetchall()
