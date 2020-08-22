import tweepy

auth = tweepy.OAuthHandler('NxuPcTKRAddOkGK6wgN4z2bPa', 'HrCNsbydnaGQQJcT0iSVUxa77bNdvuGRa9KPgSrGOPIMPn5rZo')
auth.set_access_token('1252868537162465280-gbadVxhkLsEz9FkjZZ5ccsghOiHna2', 'iSUxk5nY3luy9Adk7hUgZhYX3NGFRzikrJrp7xyFPCnEh')

api = tweepy.API(auth)
user= api.me()

print(user.name)
print(user.screen_name)
print(user.followers_count)