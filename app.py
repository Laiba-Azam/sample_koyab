from flask import Flask, send_from_directory
import os

app = Flask(__name__)

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
