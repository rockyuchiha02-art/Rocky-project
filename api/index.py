from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "success": True,
        "message": "Hello from Vercel + Flask!"
    }

@app.route("/otp")
def otp():
    return {
        "success": True,
        "otp": "API is working"
    }

# Vercel looks for the WSGI app object named "app"
