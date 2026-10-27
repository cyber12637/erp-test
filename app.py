from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style='text-align: center; margin-top: 50px; font-family: Arial, sans-serif;'>
        <h1 style='color: #2e7d32;'>ERP System Online!</h1>
        <p>Render par Python Web Service perfectly live chal rahi hai.</p>
        <span style='padding: 8px 16px; background: #e8f5e9; border: 1px solid #4caf50; border-radius: 6px;'>
            Status: Active 24/7
        </span>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
