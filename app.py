from flask import Flask, render_template, request 
import urllib.parse

app = Flask(__name__)

def remove_non_numeric(value):
  cleaned_value = ''
  for char in value:
    if char.isdigit():
      cleaned_value += char
  return cleaned_value

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/whatsapp-link-generator', methods=['POST'])
def generate_link():
  country_code = request.form['country_code']
  phone_number = request.form['phone_number']
  whatsapp_message = request.form['whatsapp_message']
  
  country_code_clean = remove_non_numeric(country_code)
  phone_number_clean = remove_non_numeric(phone_number)

  message_encoded = urllib.parse.quote(whatsapp_message)

  link = f"https://api.whatsapp.com/send?phone={country_code_clean}{phone_number_clean}&text={message_encoded}"

  return render_template('result.html', link=link)

if __name__ == '__main__':
  app.run()
