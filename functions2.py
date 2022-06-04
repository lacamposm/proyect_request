#!/usr/bin/env python3.8
import requests

##
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJydVwEAAAAAIL7KbqUsfX8Y%2BfPFBaJJQC7BSLI%3D66l1uuozkA0UP4PWUzWfPROYM1KM2iaMUdPKhnuCxQfV4JzRfS'
BASE_URL = "https://api.twitter.com/2"
end_point_users = "/users/"
end_point_tweets = "/tweets"
url = end_point_users + "by?usernames=lacamposm,villalobossebas&expansions=pinned_tweet_id"
######################################################################################################
 
def make_get_request(endpoint, params):
    url = BASE_URL + endpoint + params
    r1 = requests.get(url, headers={"Authorization": "Bearer " + bearer_token})
    print(r1.json())

make_get_request(end_point_users, "by?usernames=lacamposm")
