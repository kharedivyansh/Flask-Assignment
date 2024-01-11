from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None  # Default value if there is no user input yet

    if request.method == 'POST':
        user_input = request.form.get('user_input')

    return render_template('index.html', user_input=user_input)

if __name__ == '__main__':
    app.run(host = "0.0.0.0")

