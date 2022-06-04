#!/usr/bin/env python3.8
import pandas as pd
import numpy as np
import requests

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
##
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJydVwEAAAAAIL7KbqUsfX8Y%2BfPFBaJJQC7BSLI%3D66l1uuozkA0UP4PWUzWfPROYM1KM2iaMUdPKhnuCxQfV4JzRfS'
############## Este es protocolo de conexión. #############
end_point_users = "https://api.twitter.com/2/users/"
######################################################################################################
url = end_point_users + "by?usernames=lacamposm,villalobossebas&expansions=pinned_tweet_id"
r1 = requests.get(url, headers={"Authorization": "Bearer " + bearer_token})
print(r1.json())
######################################################################################################
mentions = "637189539/mentions?tweet.fields=created_at,author_id,public_metrics&max_results=100"
expansions = "&expansions=referenced_tweets.id"
r2 = requests.get(end_point_users+mentions+expansions, headers={"Authorization":"Bearer " + bearer_token})
######################################################################################################
def get_id(username):
    url = "https://api.twitter.com/2/users/by?usernames="+username
    r = requests.get(url,headers={"Authorization": "Bearer " + bearer_token})
    return r.json()["data"][0]["id"]
get_id("lacamposm")
######################################################################################################
def get_all_tweets(username):
    base_url = "https://api.twitter.com/2/users/"
    username = get_id(username)
    expansions = "&expansions=referenced_tweets.id"
    request = "/tweets?tweet.fields=created_at,author_id,public_metrics&max_results=100"
    url = base_url + username + request + expansions ## Check the firts page.
    ###
    r = requests.get(url, headers={"Authorization": "Bearer " + bearer_token})
    df = pd.DataFrame(r.json()["data"])
    while r.json()["meta"]["result_count"]==100:        
        next_token = "&pagination_token=" + r.json()["meta"]["next_token"]
        print(url)
        url = url + next_token
        print(url)
        r = requests.get(url, headers={"Authorization": "Bearer " + bearer_token})
        df = df.append(pd.DataFrame(r.json()["data"]), ignore_index= True)
    return df

print(get_all_tweets("lacamposm"))