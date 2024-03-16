from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

# Route for your HTML files
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/reminder')
def reminder():
    return render_template('reminder.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

if __name__ == '__main__':
    app.run(debug=True)