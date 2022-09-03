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
