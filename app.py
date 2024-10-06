from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re, os

app = Flask(__name__)
mail = Mail(app)
app.secret_key = os.environ.get('SECRET_KEY')

# Simple email validation pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+$'

#app configuratin for the mail sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('DEFAULT_SENDER')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/office-relocation')
def office_relocation():
  return render_template('office-relocation.html')

@app.route('/household-shifting')
def household_shifting():
  return render_template('household-shifting.html')

@app.route('/loading-unloading')
def loading_unloading():
  return render_template('loading-unloading.html')

@app.route('/packing-and-moving')
def packing_moving():
  return render_template('packing-moving.html')

@app.route('/pre-moving-survey')
def pre_moving_survey():
  return render_template('pre-moving-survey.html')

@app.route('/transportation')
def transportation():
  return render_template('transportation.html')

@app.route('/request-quote')
def request_quote():
  return render_template('request-quote.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact-us')
def contact_us():
  return render_template('contact-us.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

# @app.route('/submit-quote', methods=['POST'])
# def submit_quote():
#   name = request.form['name']
#   email = request.form['email']
#   phone = request.form['phone']
#   moving_date = request.form['movingDate']
#   origin = request.form['origin']
#   destination = request.form['destination']
#   special_requests = request.form['specialRequests']

#   # Server-side validation
#   if not name or not email or not phone or not moving_date or not origin or not destination:
#     flash('All fields are required', 'error')
#     return redirect(url_for('request_quote'))

#   if not re.match(email_pattern, email):
#     flash('Invalid email address', 'error')
#     return redirect(url_for('request_quote'))

#   # Save the data to a database or perform further processing here

#   # For this example, we'll just print the data
#   print(f'Name: {name}')
#   print(f'Email: {email}')
#   print(f'Phone: {phone}')
#   print(f'Moving Date: {moving_date}')
#   print(f'Origin: {origin}')
#   print(f'Destination: {destination}')
#   print(f'Special Requests: {special_requests}')

#   flash('Quote request submitted successfully', 'success')
#   return redirect(url_for('request_quote'))

@app.route('/submit-quote', methods=['POST'])
def submit():
  # Get form data
  name = request.form['name']
  email = request.form['email']
  phone = request.form['phone']
  moving_date = request.form['moving-date']
  from_address = request.form['from-address']
  to_address = request.form['to-address']

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
    subject = 'Successful Submission'
    body = 'Your request has been successfully submitted.'

    send_email(subject, email, body,from_address,to_address)

    return 'Success'
    # return redirect(url_for('thank_you'))


def send_email(subject, recipient, body,from_address,to_address):
  msg = Message(subject,
                sender='chdivakardiva192000@gmail.com',
                recipients=[recipient])
  msg.body = body
  mail.send(msg)

# @app.route('/thank_you')
# def thank_you():
#   msg = Message('Hello from the other side!',
#                 sender='chdivakardiva192000@gmail.com',
#                 recipients=['chdivakardiva192000@gmail.com'])
#   msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#   mail.send(msg)
#   return "Message sent!"

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)