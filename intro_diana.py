#!/usr/bin/env python3.8
import requests
#help(requests)
r = requests.get('https://www.python.org')
#r1 = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.text)
#json_response_body = r.json()
#text_response = r.text
#print(type(text_response))
#print(type(json_response_body))
##########################################################################################
url  = 'https://api.twitter.com/2/users/by?usernames=lacamposm,twitterapi,adsapi&expansions=pinned_tweet_id&tweet.fields=author_id,created_at'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJydVwEAAAAAIL7KbqUsfX8Y%2BfPFBaJJQC7BSLI%3D66l1uuozkA0UP4PWUzWfPROYM1KM2iaMUdPKhnuCxQfV4JzRfS'
#r1 = requests.get(url, headers={'Authorization': 'Bearer ' + bearer_token})
print("holaaaaaaaaaaaaaaaaaaa")
print(r1.json())
##########################################################################################
#url2 = "https://api.twitter.com/2/users/637189539/mentions?expansions=referenced_tweets.id&tweet.fields=created_at,author_id,text,lang&max_results=100"
#r2 = requests.get(url2, headers={'Authorization': 'Bearer ' + bearer_token})
#print(r2.json())

#curl "https://api.twitter.com/2/users/637189539/mentions?expansions=referenced_tweets.id&tweet.fields=created_at,author_id,text,lang&max_results=100"

## https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions
## Menciones a un cliente y con los parámetros se obtiene los tweets relacionados.
#mentions_andres = client.get_users_mentions(id = andres_id, max_results = 100,
#                                           tweet_fields = ["text","created_at","author_id",],
#                                            expansions = ["referenced_tweets.id"])
