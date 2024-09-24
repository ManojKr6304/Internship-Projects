from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error:
        matches = ["Invalid regex pattern"]
    return render_template('index.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(regex_email, email):
            result = "Valid email"
        else:
            result = "Invalid email"
        return render_template('email_validation.html', result=result)
    return render_template('email_validation.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
