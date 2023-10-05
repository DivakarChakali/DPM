from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/requestquote')
def request():
  return render_template('quote.html')

@app.route('/aboutus')
def about():
  return render_template('about.html')

@app.route('/contactus')
def contact():
  return render_template('contact.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
