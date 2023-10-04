import praw

from os import getenv as genv
from dotenv import load_dotenv


load_dotenv()
reddit = praw.Reddit(client_id=genv("CLIENTID"), \
                     client_secret=genv("CLIENT_SECRET"), \
                     user_agent=genv("USER_AGENT"), \
                     username=genv("USERNAME1"), \
                     password=genv("PASSWD"))


print(reddit.read_only)

file = open("var.txt", "w")


fields = [(submission.title, submission.selftext) for submission in reddit.subreddit("test").hot(limit=10)]


file.close()