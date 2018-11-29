#GGG replybot v1
#this bot relies on you having an edited praw.ini file that has your OAuth2 information stored
import praw
import pdb
import re
import os

#create a praw instance of Reddit
reddit = praw.Reddit('g_bot')

#keep track of posts using a list
if not os.path.isfile("prt.txt"):
    prt = []
#else read and split on unique post id
else:
    with open("prt.txt", "r") as f:
        prt = f.read()
        prt = prt.split("\n")
        prt = list(filter(None, prt))

subreddit = reddit.subreddit('pathofexile')
for submission in subreddit.new(limit = 5):
    if submission.id not in prt: