import sqlite3 as sql

def main():
    try:
       db = sql.connect('TelefonDefteri.db')
       print("Database created")
    except:
        print("failed to create database")
    finally:
        db.close()

if __name__ == "__main__":
    main()