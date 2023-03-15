import os
import pandas as pd
import praw

from dotenv import load_dotenv

def auth_reddit():
    load_dotenv()
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_SECRET = os.getenv('REDDIT_SECRET')
    REDDIT_DEVELOPER_NAME = os.getenv('REDDIT_DEVELOPER_NAME')

    return praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_SECRET, user_agent=REDDIT_DEVELOPER_NAME)

if __name__ == "__main__":
    reddit = auth_reddit()

    posts = []
    soccer_subreddit = reddit.subreddit('soccer')
    for post in soccer_subreddit.hot(limit=10):
        posts.append([
                        post.title,
                        post.score,
                        post.id,
                        post.subreddit,
                        post.url,
                        post.num_comments,
                        post.selftext,
                        post.created
                    ])

    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    print(posts)
