#import library
import sqlite3

class db_operations():

    #constructor
    def __init__(self, conn_path):
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        #print("connection made ...")

    def single_record(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def bulk_insert(self, query, records):
        self.cursor.executemany(query, records)
        self.connection.commit()
        print("query executed")

    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results
    
    def name_placeholder_query(self, query, dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results

    #a function that executes a single query of any language and can return a whole tuple
    def execute_one(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()

    #destructor
    def destructor(self):
        self.connection.close()

    def tablesql():
      Create_Table_Query = '''
        CREATE TABLE Song_Data(
            SongID VARCHAR(30) PRIMARY KEY NOT NULL,
            Name VARCHAR(30) NOT NULL,
            Artist VARCHAR(30),
            Danceability FLOAT,
            Energy FLOAT,
            Song_Key FLOAT,
            Loudness FLOAT,
            Song_Mode FLOAT,
            Speechiness FLOAT,
            Acousticness FLOAT,
            Instrumentalness FLOAT,
            Liveness FLOAT,
            Valence FLOAT,
            Tempo FLOAT,
            Share_Link VARCHAR(220) NOT NULL
        );
      '''