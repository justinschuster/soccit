import os
import praw

from dotenv import load_dotenv

load_dotenv()
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')
REDDIT_DEVELOPER_NAME = os.getenv('REDDIT_DEVELOPER_NAME')

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_SECRET, user_agent=REDDIT_DEVELOPER_NAME)
