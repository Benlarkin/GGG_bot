#GGG replybot v1
#this bot relies on you having an edited praw.ini file that has your OAuth2 information stored
import praw
import pdb
import re
import os
import smtplib

#create a praw instance of Reddit
reddit = praw.Reddit('g_bot')
#create a server instance via SMTP gmail to send emails
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("youremail/username", "yourpassword")
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
#check the 5 new posts each instance (plan to run every minute on the minute)
for submission in subreddit.new(limit = 5):
    #making sure we havne't checked this post yet
    if submission.id not in prt:
        #obtian te url so we can include it in the email
        postlink = submission.url
        #three main content contributors from Grinding Gear Games(handle all PR)
        if submission.author == "Bex_GGG" or "Mark_GGG" or "chris_wilson":
            msg = "new post by GGG! link: " + postlink
            server.sendmail("you@gmail.com", "target@example.com", msg)
