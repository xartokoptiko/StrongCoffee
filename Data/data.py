"""

    @Description:
        - This file is for handling data from a single sql file so that users projects and options
        are saved for a better experience

"""
import sqlite3


class Data:
    def __init__(self):
        self.connection = sqlite3.connect("Data/data.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Projects (project_name TEXT
        , project_dir TEXT, created DATE, updated DATE) 
    """)
        self.connection.commit()

    def save_new_project(self, project_name, project_dir):
        self.cursor.execute("""INSERT INTO Projects(project_name, project_dir, created, updated)
         VALUES (?,?, strftime('%Y-%m-%d %H-%M-%S','now'), strftime('%Y-%m-%d %H-%M-%S','now') )""", (project_name, project_dir))
        self.connection.commit()

    def drop_table(self):
        self.cursor.execute("DROP TABLE Projects")
        self.connection.commit()

    def update_now(self, project_name):
        self.cursor.execute("""UPDATE Projects SET updated=strftime('%Y-%m-%d %H-%M-%S','now') WHERE project_name=? """,
                            [project_name])
        self.connection.commit()

    def get_projects(self):
        self.cursor.execute("SELECT * FROM Projects")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
        print("--Connection to Data Base Closed!")
