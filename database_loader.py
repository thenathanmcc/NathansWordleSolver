#!/bin/env python3
"""
A simple script to load data from a text file into a PostgreSQL database.
Written by Nathan McCulloch
"""
import psycopg2
from psycopg2 import Error


"""
Database connection parameters
"""
DATABASE_USER = "test"
DATABASE_USER_PASSWORD = "test_password"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "5432"
DATABASE_NAME = "dictionary_db"

INSERT_QUERY = "INSERT INTO words (word) VALUES ('%s');"

TEXT_FILE = "words.txt"

def populate_db(txt_file, ins_query):
    try:
        # Attempt to establish connection with the database server
        connection = psycopg2.connect( 	user=DATABASE_USER,
                                        password=DATABASE_USER_PASSWORD,
                                        host=DATABASE_HOST,
                                        port=DATABASE_PORT,
                                        database=DATABASE_NAME )
        cursor = connection.cursor()
        word_count = 0

        with open("./words.txt") as word_file:
            lines = word_file.readlines()
            for line in lines:
                line = line.strip('\n')
                if len(line) == 5:
                    cursor.execute(ins_query % (line))
                    word_count += 1
        
        print("Inserted %s words" % word_count)
        connection.commit() # Commit transaction

    except (Exception, Error) as error:
        print("Error connecting to PostgreSQL:\n", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")

if __name__ == "__main__":
    populate_db(TEXT_FILE, INSERT_QUERY)