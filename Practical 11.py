import sqlite3 as sql


class StudentInfo:
    def __init__(self):
        self.con = sql.connect('database.db')
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS StudentInfo (id INTEGER, name TEXT, course TEXT)")

    def insert(self, id, name, branch):
        self.cursor.execute("INSERT INTO StudentIfo values (?,?,?)", (id, name, branch))

    def display(self, id):
        self.cursor.execute("SELECT * FROM StudentInfo WHERE id=?", id)
        Id, name, branch = self.cursor.fetchall()
        print('ID :', Id)
        print('Name :', name)
        print('Branch', branch)

    def update_name(self, id, name):
        self.cursor.execute('UPDATE StudentInfo SET course = (?) where name =(?)', (name, id))




