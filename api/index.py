from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "success": True,
        "message": "Hello from Vercel + Flask!"
    }

# Vercel looks for the WSGI app object named "app"
