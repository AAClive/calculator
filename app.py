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
from flask import redirect
from email.message import EmailMessage
from selenium.webdriver.chrome.service import Service
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(("192.168.15.180",5050))
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
  if request.method=="POST":
    variable = request.form.get("variable")
    server.send(
  render_template("home.html")
