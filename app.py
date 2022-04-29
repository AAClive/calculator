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
