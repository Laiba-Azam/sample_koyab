from flask import Flask, jsonify, render_template
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def draw_petal(num_petals, radius, angle):
    """Draws a single petal of the flower."""
    theta = np.linspace(angle - np.pi / 4, angle + np.pi / 4, 100)
    r = radius * np.cos(2 * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def draw_flower(num_petals, radius):
    """Draws the entire flower."""
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    for i in range(num_petals):
        angle = 2 * np.pi * i / num_petals
        x, y = draw_petal(num_petals, radius, angle)
        ax.plot(x, y, color='red')

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_data = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return f"data:image/png;base64,{plot_data}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flower', methods=['GET'])
def get_flower():
    flower_image = generate_flower(5, 2)  # Example: 5 petals, radius 2
    message = "In a world of boys he is a gentle man My Batman"
    return jsonify({'flower_image': flower_image, 'message': message})

def generate_flower(num_petals, radius):
    """Generates the flower image and returns it as base64."""
    return draw_flower(num_petals, radius)

if __name__ == '__main__':
    app.run(debug=True)
