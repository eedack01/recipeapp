# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:57:16 2020

@author: User
"""

import sqlite3
from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/showrecipes')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM recipes').fetchall()
    return render_template('index.html', items=posts)

@app.route('/searchrecipes',methods=['Get','POST'])
def search():
    conn = get_db_connection()
    cur = conn.cursor()
    name = request.form['searchrecipes']
    cur.execute("select * from recipes where [name] like ?",('%'+name+'%',))
    rows = cur.fetchall()
    conn.commit()
    return render_template('index.html', items = rows)
  
@app.route('/addrecipe',methods=['Get','POST'])
def addrecipe(): #page to insert data
    return render_template('form.html')

@app.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    conn = get_db_connection()
    cur = conn.cursor()
    rows = cur.execute("select * from recipes where id = ?",(recipe_id,)).fetchone()
    conn.commit()
    return render_template('result.html',items=rows)

@app.route('/recipe/delete/<int:recipe_id>', methods=['POST'])
def deleterecipe(recipe_id):
    get_db_connection()
    conn = get_db_connection()
    cur = conn.cursor()
    rows = cur.execute("delete from recipes where id = ?",(recipe_id,)).fetchone()
    conn.commit()
    return redirect(url_for('index'))
    
@app.route('/insertrecipe',methods=['GET', 'POST'])
def insertrecipe(): #insert data
    get_db_connection()
    name = request.form['name']
    cookingtime = request.form['cookingtime']
    ingredients = request.form['ingredients']
    instructions = request.form['instructions']
    conn = get_db_connection()
    insert = 'insert into recipes (name,cookingtime,ingredients,instructions) values(?,?,?,?)'
    posts = conn.execute(insert,(name,cookingtime,ingredients,instructions))
    conn.commit()
    return render_template('form.html')


    

if __name__ =='__main__':
    app.debug = True
    app.run()