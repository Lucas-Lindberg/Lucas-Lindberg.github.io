from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '1234'

users = {
    "Lucas Lindberg": "1234",
    "Maximilian Karlsson": "1337",
    "Wincent Karlsson": "6969",
    "Isak Wennberg": "0000"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    if not session.get('authenticated'):
        return redirect(url_for('loading'))

    return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['authenticated'] = True
        session['password'] = password
        return redirect(url_for('success'))
    else:
        return render_template('failure.html')

@app.route('/loading')
def loading():
    if not session.get('authenticated'):
        return redirect(url_for('index'))

    password = session.get('password', '')
    return render_template('loading.html', password=password)

@app.route('/start')
def start():
    if not session.get('authenticated'):
        return redirect(url_for('index'))

    return render_template('start.html')

@app.route('/self_destruct')
def self_destruct():
    return render_template('self_destruct.html')

@app.route('/aftermath')
def aftermath():
    return render_template('aftermath.html')

if __name__ == '__main__':
    app.run(debug=True)

