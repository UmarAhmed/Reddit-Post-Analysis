import praw
import requests
import datetime

# N is the number of posts to be used
N = 10000
secret = ""
username = ""
clientID = ""
reddit = praw.Reddit(user_agent='nani (by /u/USERNAME)',
                     client_id=clientID, client_secret=secret,
                     username=username, password='')

subreddit = reddit.subreddit('askreddit')

r = requests.get(
    'http://www.reddit.com/r/{}.json'.format(subreddit),
    headers={'user-agent': 'Mozilla/5.0'})



data = [[i.title,i.score, datetime.datetime.fromtimestamp(i.created)] for i in subreddit.hot(limit=N)]


with open('titles.txt', mode="w") as outfile:  
    for i in data:
        outfile.write("%s\n" % i[0])

with open('scores.txt', mode="w") as outfile:  
    for i in data:
        outfile.write("%s\n" % i[1])

with open('times.txt', mode="w") as outfile:  
    for i in data:
        outfile.write("%s\n" % i[2])


