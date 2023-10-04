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


fields = []

for submission in reddit.subreddit("ich_iel").hot(limit=10):
    if len(submission.selftext) == 0 and len(submission.url) != 0:
        fields.append([submission.title, submission.url])
    else:
        fields.append([submission.title, submission.selftext])
    #file.write(str(vars(submission)) + "\n\n")



file.close()