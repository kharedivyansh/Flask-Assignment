# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(host= "0.0.0.0")