import sqlite3 as sql


class StudentInfo:
    def __init__(self):
        self.con = sql.connect('database.db')
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS StudentInfo (id INTEGER, name TEXT, branch TEXT)")
        self.con.commit()

    def insert(self):
        id = int(input('Enter ID :'))
        name = input('Enter Name : ')
        branch = input('Enter Branch : ')
        self.cursor.execute("INSERT INTO StudentInfo values (?,?,?)", (id, name, branch))
        self.con.commit()

    def display(self):
        id  = int(input('Enter ID : '))
        self.cursor.execute("SELECT * FROM StudentInfo WHERE id=?", (id,))
        for Id, name, branch in  self.cursor.fetchall():
            print('ID :', Id)
            print('Name :', name)
            print('Branch', branch)

    def update(self):
        id = int(input('Enter ID :'))
        name = input('Enter Name : ')
        branch = input('Enter Branch : ')
        self.cursor.execute('UPDATE StudentInfo SET name = ?, branch = ? where id =?', (name, branch, id))
        self.con.commit()

    def delete(self):
        id = int(input('Enter ID : '))
        self.cursor.execute('DELETE FROM StudentInfo where id = ?', (id,))
        self.con.commit()

    def display_all(self):
        self.cursor.execute('SELECT * FROM StudentInfo')
        print('ID \t', 'Name \t', 'Branch')
        for Id, name, branch in  self.cursor.fetchall():
            print(Id,'\t',name,'\t',branch)

if __name__ == '__main__':
    sinfo = StudentInfo()
    sinfo.insert()
    sinfo.update()
    sinfo.delete()
    sinfo.display_all()





