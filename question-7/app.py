from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()

@app.route('/')
def index():
    db = get_db()
    cursor = db.execute('SELECT * FROM items')
    items = cursor.fetchall()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        title = request.form['title']
        db = get_db()
        db.execute('INSERT INTO items (title) VALUES (?)', (title,))
        db.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        db.execute('UPDATE items SET title = ? WHERE id = ?', (title, item_id))
        db.commit()
        return redirect(url_for('index'))
    else:
        cursor = db.execute('SELECT * FROM items WHERE id = ?', (item_id,))
        item = cursor.fetchone()
        return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    db = get_db()
    db.execute('DELETE FROM items WHERE id = ?', (item_id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.teardown_appcontext(close_db)
    if not os.path.exists(app.config['DATABASE']):
        init_db()
    app.run(debug=True)
