from flask import (
    Flask, render_template
)
from flask_cors import CORS



app = Flask(__name__)
app.secret_key = "supersecret"

CORS(app, supports_credentials=True)

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax"
)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
