import logging
from flask import Flask, request, jsonify
from post import Post
from yodelrservice import YodelrService
import time

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

    current_timestamp = int(time.time())    
    yodelrService.add_post(user_name, post_text, current_timestamp)

    return jsonify({"message": "Post added successfully"}), 201

@app.route("/deleteuser", methods=['POST'])
def delete_user():
    app.logger.info("/deleteuser")
    data = request.get_json()
    user_name = data.get('user_name')
    
    if not user_name:
        return jsonify({"error": "user_name is required"}), 400
    
    if not yodelrService.user_exists(user_name):
        return jsonify({"error": "That user_name does not exist"}), 400
    
    yodelrService.delete_user(user_name)

    return jsonify({"message": "User deleted successfully"}), 200

@app.route("/getpostsforuser", methods=['GET'])
def get_posts_for_user():
    app.logger.info("/getpostsforuser")
    user_name = request.args.get('user_name')
    
    if not user_name:
        return jsonify({"error": "user_name is required"}), 400
    
    posts = yodelrService.get_posts_for_user(user_name)

    return jsonify({"posts": posts}), 200

@app.route("/getpostsfortopic", methods=['GET'])
def get_posts_for_topic():
    app.logger.info("/getpostsfortopic")
    topic = request.args.get('topic')
    
    if not topic:
        return jsonify({"error": "topic is required"}), 400
    
    posts = yodelrService.get_posts_for_topic(topic)

    return jsonify({"posts": posts}), 200

@app.route("/gettrendingtopics", methods=['GET'])
def get_trending_topics():
    app.logger.info("/gettrendingtopics")
    from_timestamp = request.args.get('from_timestamp')
    to_timestamp = request.args.get('to_timestamp')
    
    if not from_timestamp or not to_timestamp:
        return jsonify({"error": "from_timestamp and to_timestamp are required"}), 400
    
    trending_topics = yodelrService.get_trending_topics(int(from_timestamp), int(to_timestamp))

    return jsonify({"trending_topics": trending_topics}), 200

if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    app.run(debug=True)




