from flask import Flask
app = Flask(__name__)
# secret key
app.secret_key = "killing me smalls"