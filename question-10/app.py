from flask import Flask, render_template

app = Flask(__name__)

# Custom error handlers

# 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Route to generate a 500 error for testing
@app.route('/generate_error')
def generate_error():
    raise Exception("This is a test 500 error")

# Main route
@app.route('/')
def index():
    return 'Welcome to the Flask Error Handling Example!'

if __name__ == '__main__':
    app.run(debug=True)
