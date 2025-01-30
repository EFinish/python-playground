import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flask-app")

app = Flask(__name__)
app.logger = logger

logger.info("Server starting...")

@app.route("/")
def hello_world():
    app.logger.info("Received request at /")
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    app.run(debug=True)




