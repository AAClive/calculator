from flask import Flask
from flask import render_template
from flask import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.chrome.service import Service
chrome_options=webdriver.ChromeOptions()
chrome_options.binary_loction=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
driver=webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")),options=chrome_options))


app=Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

if __name__=="__main__":
  app.run()
 
