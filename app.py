import os
from flask import Flask, render_template

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for About Us page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Main block for deployment (bind to 0.0.0.0 and use dynamic port)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
