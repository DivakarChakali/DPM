from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re, os

app = Flask(__name__)
mail = Mail(app)
app.secret_key = os.environ.get('SECRET_KEY')
admail = os.environ.get('amail')

# Simple email validation pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+$'

#app configuratin for the mail sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
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

@app.route('/services/office-relocation')
def office_relocation():
  return render_template('office-relocation.html')

@app.route('/services/household-shifting')
def household_shifting():
  return render_template('household-shifting.html')

@app.route('/services/loading-unloading')
def loading_unloading():
  return render_template('loading-unloading.html')

@app.route('/services/packing-and-moving')
def packing_moving():
  return render_template('packing-moving.html')

@app.route('/services/pre-moving-survey')
def pre_moving_survey():
  return render_template('pre-moving-survey.html')

@app.route('/services/transportation')
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

@app.route('/submit-quote', methods=['POST'])
def submit_rform():
  data = request.form
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
    try:
      # database.insert_data(data)
      email_notification(name, email, phone, moving_date, origin, destination,
                         special_requests)
      # Flash a success message
      flash("Your quotation request has been submitted successfully!",
            "success")
      return redirect(url_for('home'))
    except Exception as e:
      return f'Error: {str(e)}'

@app.route('/submit-cform', methods=['POST'])
def submitcform():
  cdata = request.form
  name = request.form['name']
  email = request.form['email']
  message = request.form['message']
  cerrors = []

  email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

  if not name:
    cerrors.append('Name is required')
  if not re.match(email_pattern, email):
    cerrors.append('Invalid email format')

  if cerrors:
    return render_template('home.html', errors=cerrors)
  else:
    try:
      # database.insert_data_details(cdata)
      send_email_notification(name, email, message)
      # Flash a success message
      flash("Your contact request has been submitted successfully!", "success")
      return redirect(url_for('home'))
    except Exception as e:
      return f'Error: {str(e)}'


def send_email_notification(name, email, message):
  msg = Message(subject='contact request conformation', recipients=[email])
  msg.html = render_template('mail-templates/cmail.html',
                             name=name,
                             email=email,
                             message=message)
  mail.send(msg)
  # adminNC(name, email, message)


def email_notification(name, email, phone, moving_date, origin, destination,
                       special_requests):
  msg = Message(subject='Acknowledgement from Divakarpackersandmover.com',
                recipients=[email])
  msg.html = render_template('mail-templates/rmail.html',
                             name=name,
                             email=email,
                             phone=phone,
                             moving_date=moving_date,
                             origin=origin,
                             destination=destination,
                             special_requests=special_requests)
  mail.send(msg)
  # adminNR(name, email, phone, moving_date, origin, destination,
  #         special_requests)

# def adminNC(cname, cemail, cmessage):
#   msg = Message(subject='New contact request received', recipients=[admail])
#   msg.html = render_template('mail-templates/amc.html',
#                              name=cname,
#                              email=cemail,
#                              message=cmessage)
#   mail.send(msg)


# def adminNR(name, email, phone, moving_date, origin, destination,
#             special_requests, admail):
#   msg = Message(subject='New quotation request received', recipients=[admail])
#   msg.html = render_template('mail-templates/amr.html',
#                              name=name,
#                              email=email,
#                              phone=phone,
#                              moving_date=moving_date,
#                              origin=origin,
#                              destination=destination,
#                              special_requests=special_requests)
#   mail.send(msg)


@app.route('/thanks')
def thanks():
  response = app.make_response(render_template('thanks.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response

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