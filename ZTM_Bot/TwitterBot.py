import tweepy
import time

auth = tweepy.OAuthHandler('NxuPcTKRAddOkGK6wgN4z2bPa', 'HrCNsbydnaGQQJcT0iSVUxa77bNdvuGRa9KPgSrGOPIMPn5rZo')
auth.set_access_token('1252868537162465280-gbadVxhkLsEz9FkjZZ5ccsghOiHna2',
                      'iSUxk5nY3luy9Adk7hUgZhYX3NGFRzikrJrp7xyFPCnEh')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'xyz':
        if follower.followers_count> 100:
            follower.follow()
            break
    # print(follower.name)
