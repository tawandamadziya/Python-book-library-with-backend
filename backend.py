import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)#("Books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    #INSERT
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO Book VALUES (NULL,?, ?, ?, ?) ", (title, author, year, isbn))
        self.conn.commit()

    #insert("The Mark", "Ymanny", 2017, 35789)
    #print(insert)


    #DELETE
    def delete(self, ISBN):
        self.cur.execute("DELETE FROM Book WHERE ISBN = ?", (ISBN))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows


    #UPDATE
    def update(self, title, year, author, ISBN):
        self.cur.execute("UPDATE Book SET title=? year=? author=? WHERE ISBN=?", (title, year, author, ISBN))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows



    #SEARCH
    def search(self, title, year, author, ISBN):
        self.cur.execute("SELECT * FROM search WHERE title=? OR year=? OR author=? OR ISBN=? ", (title, year, author, ISBN))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    #VIEW ALL
    def view_db(self):
        self.cur.execute("SELECT * FROM Book")
        rows = self.cur.fetchall()
        return rows



def __del__(self):
    self.conn.close()        
