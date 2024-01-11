from flask import Flask , render_template
app = Flask(__name__)

@app.route('/greet/<name>')
def greet_func(name):
    return render_template('index.html',name=name)

if (__name__)== ("__main__"):
    app.run(host= "0.0.0.0")