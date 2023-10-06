from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'BD9C8CDB5A98EEDA'

# Simple email validation pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+$'


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/thank_you')
def thank_you():
  return 'Thank you for your submission!'


@app.route('/aboutus')
def about():
  return render_template('about_us.html')


@app.route('/contactus')
def contact():
  return render_template('contact_us.html')


@app.route('/faq')
def faq():
  return render_template('faq.html')


@app.route('/requestquote')
def requestquote():
  return render_template('request_quote.html')


@app.route('/submit_quote', methods=['POST'])
def submit_quote():
  name = request.form['name']
  email = request.form['email']
  phone = request.form['phone']
  moving_date = request.form['movingDate']
  origin = request.form['origin']
  destination = request.form['destination']
  special_requests = request.form['specialRequests']

  # Server-side validation
  if not name or not email or not phone or not moving_date or not origin or not destination:
    flash('All fields are required', 'error')
    return redirect(url_for('request_quote'))

  if not re.match(email_pattern, email):
    flash('Invalid email address', 'error')
    return redirect(url_for('requestquote'))

  # Save the data to a database or perform further processing here
  # For this example, we'll just print the data
  print(f'Name: {name}')
  print(f'Email: {email}')
  print(f'Phone: {phone}')
  print(f'Moving Date: {moving_date}')
  print(f'Origin: {origin}')
  print(f'Destination: {destination}')
  print(f'Special Requests: {special_requests}')

  flash('Quote request submitted successfully', 'success')
  return redirect(url_for('requestquote'))


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
