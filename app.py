from flask import Flask, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

def get_db_connection():
    conn = sqlite3.connect('database/init_db.py')
    conn.row_factory = sqlite3.Row
    return conn

# главная страница(товары)
@app.route('/') # декоратор. Когда польз. заходит на адрес /(гл.стр.) вызывается функция ниже
def index(): # '/' - корень сайта
    conn = get_db_connection
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)


# добавление товара в корзину
@app.route('/add/add_to_cart/<int: product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)