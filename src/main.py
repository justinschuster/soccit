import os
import pandas as pd

from pipeline_package.utils import auth_reddit

if __name__ == "__main__":
    reddit = auth_reddit()

    posts = []
    soccer_subreddit = reddit.subreddit('soccer')
    for post in soccer_subreddit.hot(limit=10):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    os.makedirs('/home/justin/Projects/scrape_r_soccer/output', exist_ok=True)
    posts.to_csv('/home/justin/Projects/scrape_r_soccer/output/out.csv')
