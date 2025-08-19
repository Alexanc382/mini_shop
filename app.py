from flask import Flask

app = Flask(__name__)


@app.route('/') # декоратор. Когда польз. заходит на адрес /(гл.стр.) вызывается функция ниже
def index(): # '/' - корень сайта


if __name__ == '__main__':
    app.run(debug=True)