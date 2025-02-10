from potato import Potato
from post import Post
import re

class PotatoService(Potato):
    __users = []
    __posts = []
    __topicPattern = re.compile(r'#([0-9a-zA-Z_]+)')

    def __init__(self):
        super().__init__()

    def user_exists(self, user_name: str) -> bool:
        return user_name in self.__users

    def add_user(self, user_name: str) -> None:
        self.__users.append(user_name)

    def add_post(self, user_name, post_text, timestamp):
        self.__posts.append(Post(user_name, post_text, timestamp))

    def delete_user(self, user_name: str) -> None:
        self.__users.remove(user_name)

        for post in self.__posts:
            if post.user == user_name:
                self.__posts.remove(post)

    
    def get_posts_for_user(self, user_name: str):
        postsTexts = []

        for post in self.__posts:
            if post.user_name == user_name:
                postsTexts.append(post.post_text)

        return postsTexts
    
    def get_posts_for_topic(self, topic: str):
        postsTexts = []

        for post in self.__posts:
            if topic in self.__topicPattern.findall(post.post_text):
                postsTexts.append(post.post_text)

        return postsTexts

    def get_trending_topics(self, from_timestamp: int, to_timestamp: int):
        allTopics = {}

        for post in self.__posts:
            if from_timestamp <= post.timestamp and to_timestamp >= post.timestamp:
                postTopics = self.__topicPattern.findall(post.post_text)
                for topic in postTopics:
                    allTopics[topic] = allTopics.get(topic, 0) + 1
        
        topicsGroupedByCount = {}

        for topic in allTopics:
            count = allTopics.get(topic)
            if count in topicsGroupedByCount:
                topicsGroupedByCount[count].append(topic)
            else:
                topicsGroupedByCount[count] = [topic]
        
        sortedTopics = []

        for count in topicsGroupedByCount:
            topicsGroupedByCount[count].sort()
            sortedTopics = topicsGroupedByCount[count] + sortedTopics

        return sortedTopics


    