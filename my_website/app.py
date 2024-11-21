from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Daphne Weissfloch portfolio"
    return render_template('home.html', title=title)

@app.route('/about/')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    title = 'Contact Us'
    return render_template('contact.html', title=title)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    