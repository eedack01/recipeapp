# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:43:55 2020

@author: User
"""


import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO recipes (name, cookingtime,ingredients,instructions) VALUES (?, ?,?,?)",
            ('hot pot', '30','chilli oil','mix the stuff and boil')
            )

cur.execute("INSERT INTO recipes (name, cookingtime,ingredients,instructions) VALUES (?, ?,?,?)",
            ('Chicken jalfrezi', '45','lemon,chicken','fry chicken and make the curry yo')
            )


connection.commit()
connection.close()

