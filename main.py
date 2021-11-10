print("\nExecuting DaVis-DS")



print("\n[*] Importing packages...\n")

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from adjustText import adjust_text

import json
import os
import random
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

import credentials
import variables




print("\n[*] Loading functions, lists and dictionaries...\n")

from commands import davis_data, davis_filter, davis_label_f, davis_label_nf, davis_plot_f, davis_plot_nf

pic_path = str("result_pics/")

gen_vars = variables.gen_vars

ft_vars = variables.ft_vars
fl_vars = variables.fl_vars

cod_vars = variables.cod_vars
cn_vars = variables.cn_vars
cc_vars = variables.cc_vars

ds1_up_d = variables.ds1_up_d
ds1_se_d = variables.ds1_se_d

ds1_d = variables.ds1_d



print("\n[*] Initializing Twitter bot...\n")
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def setUpAuth():
	auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
	auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api, auth


def followStream():
	api, auth = setUpAuth()
	listener = StdOutListener()
	stream = Stream(auth, listener)
	stream.filter(track=[credentials.ACCOUNT_NAME])


print("\n    [+] DaVis-DS on line and waiting for requests.\n\n")

class StdOutListener(StreamListener):
	def on_data(self, data):
		clean_data = json.loads(data)
		user_mentions = clean_data["entities"]["user_mentions"]
		tweeted_by = clean_data["user"]["screen_name"]
		tweeted_at = clean_data["in_reply_to_screen_name"]
		try:
			tweet = clean_data['extended_tweet']["full_text"]
		except KeyError:
			tweet = clean_data['text']
		tweet_id = clean_data["id"]
        
		print("\n    [*] Possible request from user @" + tweeted_by + ":\n" + '        "' + tweet + '"\n\n')

		if user_mentions[0]["screen_name"] == credentials.ACCOUNT_NAME or user_mentions[0]["screen_name"] == credentials.ACCOUNT_NAME.lower():
			print("\n    [+] Detected username @" + credentials.ACCOUNT_NAME + " within the mentions.\n")
			respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic_path)

		elif tweeted_by != credentials.ACCOUNT_NAME and credentials.ACCOUNT_NAME in tweet:
			print("\n    [+] Detected username @" + credentials.ACCOUNT_NAME + " within the mentions.\n")
			respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic_path)
            
	def on_error(self, status):
		print("\n    [-] ERROR: " + status + "\n\n")


def respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic):
    while True:
        if "data:" in tweet.split(" "):
            try:
                davis_data(tweet)
                df = pd.read_csv("excels/df.csv")

            except NameError:
                pic = str(pic_path + 'fail.jpg')
                response = variables.err_response_data
                reply = variables.err_response + response
                break

            if "plot:" in tweet.split(" "):
                if "filter:" in tweet.split(" "):
                    try:
                        davis_filter(tweet, df)
                        davis_plot_f(tweet)

                    except KeyError:
                        pic = str(pic_path + 'fail.jpg')
                        response = variables.err_response_filter
                        reply = variables.err_response + response
                        break

                    except UnboundLocalError:
                        pic = str(pic_path + 'fail.jpg')
                        response = variables.err_response_filter
                        reply = variables.err_response + response
                        break
                    
                    except ValueError:
                        pic = str(pic_path + 'fail.jpg')
                        response = variables.err_response_vars
                        reply = variables.err_response + response
                        break

                    if "label:" in tweet.split(" "):
                        try:
                            davis_label_f(tweet)
                            plt.savefig('result_pics/plot.jpg')
                            pic = str(pic_path + 'plot.jpg')
                            reply = variables.success_response
                            break

                        except KeyError:
                            pic = str(pic_path + 'fail.jpg')
                            response = variables.err_response_label
                            reply = variables.err_response + response
                            break

                    else:
                        plt.savefig('result_pics/plot.jpg')
                        pic = str(pic_path + 'plot.jpg')
                        reply = variables.success_response
                        break

                else:
                    try:
                        davis_plot_nf(tweet, df)
                    
                    except ValueError:
                        pic = str(pic_path + 'fail.jpg')
                        response = variables.err_response_vars
                        reply = variables.err_response + response
                        break

                    if "label:" in tweet.split(" "):
                        try:
                            plt.savefig('result_pics/plot.jpg')
                            pic = str(pic_path + 'plot.jpg')
                            davis_label_nf(tweet, df)
                            reply = variables.success_response
                            break

                        except KeyError:
                            pic = str(pic_path + 'fail.jpg')
                            response = variables.err_response_label
                            reply = variables.err_response + response
                            break

                    else:
                        plt.savefig('result_pics/plot.jpg')
                        pic = str(pic_path + 'plot.jpg')
                        reply = variables.success_response
                        break

            else:
                pic = str(pic_path + 'fail.jpg')
                response = variables.err_response_command
                reply = variables.err_response + response
                break

        else:
            pic = str(pic_path + 'fail.jpg')
            response = variables.err_response_command
            reply = variables.err_response + response
            break

    postResponse(reply, tweet_id, pic)


def postResponse(reply, tweetId, pic):
	print("\n    [*] Sending...\n\n")
	api, auth = setUpAuth()
	api.update_with_media(pic, status = reply, in_reply_to_status_id = tweetId, auto_populate_reply_metadata = True)
	print("\n    [+] Response successfully sent.\n\n")


if __name__ == "__main__":
	print("\n    [*] Waiting for requests...\n")
	followStream()