import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key-12345")

# Demo ERP credentials
DEFAULT_USER = "admin"
DEFAULT_PASS = "admin123"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == DEFAULT_USER and password == DEFAULT_PASS:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password. Please try again."

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"""
    <body style="background:#0f172a;color:#f8fafc;font-family:sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;">
        <div style="background:#1e293b;padding:40px;border-radius:12px;text-align:center;border:1px solid #334155;">
            <h2 style="color:#38bdf8;">Welcome, {session['user']}!</h2>
            <p>ERP Dashboard system is active & connected.</p>
            <a href="/logout" style="color:#ef4444;text-decoration:none;font-weight:bold;">Sign Out</a>
        </div>
    </body>
    """

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
