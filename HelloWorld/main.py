from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
  return render_template('index.html')

# @app.route('/about/<username>')
# def about_page(username):
#   return f'<h1>This is the about page of {username}</h1>'

@app.route('/market')
def market_page():
  return render_template('market.html',item_name='phone')