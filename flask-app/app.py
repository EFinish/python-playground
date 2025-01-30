import logging
from flask import Flask, request, jsonify
from post import Post
from yodelrservice import YodelrService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flask-app")

app = Flask(__name__)
app.logger = logger
yodelrService = YodelrService()

logger.info("Server starting...")

@app.route("/adduser", methods=['POST'])
def add_user():
    app.logger.info("/adduser")
    data = request.get_json()
    user_name = data.get('user_name')
    
    if not user_name:
        return jsonify({"error": "user_name is required"}), 400
    
    if yodelrService.user_exists(user_name):
        return jsonify({"error": "That user_name is already taken"}), 400
    
    yodelrService.add_user(user_name)

    return jsonify({"message": "User added successfully"}), 201

@app.route("/addpost", methods=['POST'])
def add_post():
    app.logger.info("/addpost")
    data = request.get_json()
    user_name = data.get('user_name')
    post_text = data.get('post_text')

    if not user_name or not post_text:
        return jsonify({"error": "user_name and post_text are required"}), 400
    
    yodelrService.add_post(user_name, post_text, 0)

    return jsonify({"message": "Post added successfully"}), 201



if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    app.run(debug=True)




