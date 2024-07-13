from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/')
def read_file():
    try:
        with open('me.txt', 'r') as file:
            content = file.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
