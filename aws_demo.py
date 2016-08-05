from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template("home.html")
    except Exception as e:
        return str(e)
@app.route('/contact/')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
    app.run(DEBUG=True)
