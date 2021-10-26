import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute( "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT ,name text, email text , gender text , contact text , dob text , doj text , pass text , utype text , adress text , post text)" )
    con.commit()


    cur.execute( "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT ,name text, contact text , desc text )")
    con.commit()

    cur.execute( "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT ,name text )")
    con.commit()

    cur.execute( "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT ,Supplier text, Category text , Name text , Price text , qty text , Status text )" )
    con.commit()

    
create_db()    