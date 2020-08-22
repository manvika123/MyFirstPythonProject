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


search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        #tweet.retweet()
        print('I liked the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
