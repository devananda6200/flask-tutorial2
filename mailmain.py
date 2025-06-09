from flask import Flask
from flask_mail import Mail,Message
from mail_config import EMAIL_USER, EMAIL_PASS 
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_USER
app.config['MAIL_PASSWORD'] = EMAIL_PASS
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/mail')
def index():
    msg = Message("Heyyyy", sender = 'devananda6200@gmail.com', recipients = ['devanandaproff@gmail.com'])
    msg.body = "Hey Adarsh! How you doing?This is a flask generated automated email service"
    mail.send(msg)
    return "Message sent"

if __name__=='__main__':
    app.run(debug=True)