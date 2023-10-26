# hello_flask.py
from flask import *
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return '''<h1>Hello world from Flask!</h1>
    <h3> Favorite Acronym </h3>
    <p>Miguel T. : fomo (Fear of missing out) </p>'''

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2
   
@app.route('/miguel')
def t_test():
    return render_template('index.html')

