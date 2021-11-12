from credentials import davis_logo

print(davis_logo)

print("\n\033[1mEXECUTING DaVis")



print("\n[*]\033[0m Importing packages...\n")

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




print("\n\033[1m[*]\033[0m Loading functions, lists and dictionaries...\n")

from commands import davis_data, davis_filter, davis_label_f, davis_label_nf, davis_plot_f, davis_plot_nf

pic_path = credentials.pic_path
excels_path = credentials.excels_path

gen_vars = variables.gen_vars

ft_vars = variables.ft_vars
fl_vars = variables.fl_vars

cod_vars = variables.cod_vars
cn_vars = variables.cn_vars
cc_vars = variables.cc_vars

ds1_up_d = variables.ds1_up_d
ds1_se_d = variables.ds1_se_d

ds1_d = variables.ds1_d



print("\n\033[1m[*]\033[0m Initializing Twitter bot...\n")
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
        
		print("\n    \033[1m[*]\033[0m Possible request from user \033[1m@" + tweeted_by + "\033[0m:\n" + '        "' + tweet + '"\n\n')

		if user_mentions[0]["screen_name"] == credentials.ACCOUNT_NAME or user_mentions[0]["screen_name"] == credentials.ACCOUNT_NAME.lower():
			print("\n        \033[1m[+]\033[0m Detected username \033[1m@" + credentials.ACCOUNT_NAME + "\033[0m within the mentions.\n")
			respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic_path)

		elif tweeted_by != credentials.ACCOUNT_NAME and credentials.ACCOUNT_NAME in tweet:
			print("\n        \033[1m[+]\033[0m Detected username @\033[1m" + credentials.ACCOUNT_NAME + "\033[0m within the mentions.\n")
			respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic_path)
            
	def on_error(self, status):
		print("\n    \033[1;31m[-] ERROR:\033[0m " + status + "\n\n")


def respondToTweet(tweet, tweeted_by, tweeted_at, tweet_id, pic):
    print("\n        \033[1m[*]\033[0m Processing response...")
    while True:
        if "data:" in tweet.split(" "):
            try:
                davis_data(tweet)
                df = pd.read_csv(excels_path + "df.csv")

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
	print("\n        \033[1m[*]\033[0m Sending...\n\n")
	api, auth = setUpAuth()
	api.update_with_media(pic, status = reply, in_reply_to_status_id = tweetId, auto_populate_reply_metadata = True)
	print("\n            \033[1m[+] Response successfully sent.\033[0m\n\n")


if __name__ == "__main__":
	print("\n    \033[1m[+] DaVis on line and waiting for requests.\033[0m\n\n")
	followStream()
