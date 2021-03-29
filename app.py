from flask import Flask,render_template
import Shirt as s

from flask_mail import Mail, Message
from config import mail_username, mail_password

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkeywhichissupposedtobesecret"
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route("/")
def home():
    return render_template('index.html')




   
       

@app.route("/forward/", methods=['POST'])
def move_forward():  
         s.run("538.png")



@app.route('/p1/',methods=['POST'])
def p1():  
      s.run("510.jpg")
     


@app.route('/p2/',methods=['POST'])
def p2():
    s.run("512.jpg")


@app.route('/p3/',methods=['POST'])
def p3():
    s.run("519.jpg")



@app.route('/p4/',methods=['POST'])
def p4():
    s.run("520.jpg")


@app.route('/p5/',methods=['POST'])
def p5():
    s.run("544.jpg")



@app.route('/p6/',methods=['POST'])
def p6():
    s.run("549.jpg")

      
@app.route('/shop')

def shop():
    return  render_template('shop.html')


@app.route('/buy' ,methods=['GET', 'POST'])
def buy():
   
    def contact():
        if request.method == "POST":
             name = request.form.get('customername')
             productname = request.form.get('productname')
             email = request.form.get('email')
             phone = request.form.get('phone')
             address = request.form.get('address')

        msg = Message(
            subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{address}", sender=email, recipients=['mailid'])
        mail.send(msg)
        return render_template("buy.html", success=True)

    return render_template("buy.html")
  

   
       







if __name__ == '__main__':
    app.run(use_reloader = True)