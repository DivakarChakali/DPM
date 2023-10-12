from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re, os

app = Flask(__name__)
mail = Mail(app)
app.secret_key = 'BD9C8CDB5A98EEDA'

# Simple email validation pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+$'

#app configuratin for the mail sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_DEFAULT_SENDER'] = 'divakarpackers@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/services')
def services():
  return render_template('services.html')


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


quotes = []


@app.route('/submit', methods=['POST'])
def submit():
  # Get form data
  name = request.form['name']
  email = request.form['email']
  phone = request.form['phone']
  moving_date = request.form['moving_date']
  origin = request.form['origin']
  destination = request.form['destination']
  special_requests = request.form['special_requests']

  # Server-side validation
  email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  phone_pattern = r'^\d{10}$'
  errors = []

  if not name:
    errors.append('Name is required')
  if not re.match(email_pattern, email):
    errors.append('Invalid email format')
  if not re.match(phone_pattern, phone):
    errors.append('Invalid phone number format')
  if not moving_date:
    errors.append('Moving date is required')

  if errors:
    return render_template('home.html', errors=errors)
  else:
    # Store the data or send it to your backend
    quotes.append({
        'name': name,
        'email': email,
        'phone': phone,
        'moving_date': moving_date,
        'origin': origin,
        'destination': destination,
        'special_requests': special_requests
    })
    subject = 'Successful Submission'
    recipient = quotes[1]  # Replace with the recipient's email address
    body = 'Your request has been successfully submitted.'

    send_email(subject, recipient, body)

    return 'Success'
    # return redirect(url_for('thank_you'))


def send_email(subject, recipient, body):
  msg = Message(subject,
                sender='chdivakardiva192000@gmail.com',
                recipients=[recipient])
  msg.body = body
  mail.send(msg)


@app.route('/thank_you')
def thank_you():
  msg = Message('Hello from the other side!',
                sender='chdivakardiva192000@gmail.com',
                recipients=['chdivakardiva192000@gmail.com'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
