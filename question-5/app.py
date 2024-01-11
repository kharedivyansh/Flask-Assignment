from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '1234@'  # Change this to a random secret key for security

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        session['user_input'] = user_input
        return redirect(url_for('index'))

    user_input = session.get('user_input', None)
    return render_template('index.html', user_input=user_input)

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
