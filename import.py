#!/usr/bin/env python3

import csv
import sqlite3
import sys

filename = sys.argv[1]
database = sys.argv[2]
table = sys.argv[3]

conn = sqlite3.connect(database)
c = conn.cursor()

with (open(filename)) as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)
    create_statement = 'create table if not exists ' + table + ' ('

    for column in columns:
        create_statement += ' '.join(column.split('=')) + ', '
        
    create_statement = create_statement[:-2] + ')'
    c.execute(create_statement)
    
    for i,row in enumerate(reader):
        for i in range(len(row)):
            if not row[i]:
                row[i] = None
        insert_statement = 'insert into ' + table + ' values (' + '?, ' * (len(columns)-1) + '?)'
        try:
            c.execute(insert_statement, row)
        except sqlite3.Error as e:
            print("Error processing row " + str(i) + ": " + str(e))
            print(row)
            print()

conn.commit()
conn.close()
