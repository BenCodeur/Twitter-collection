import tweepy
import csv
import pandas as pd

restart = True

#####Get tweets with a specific #
def getHashtag():
    # Get the #
    print('Which # are you looking for ?')
    hashtag = input()
    # Open/Create a csv file to append datas
    csvFile = open('ua.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,q=hashtag,count=10,
                            lang="en").items(100):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

####input your tokens here to access the twitter API
consumer_key = '9Y5Tz5BiMz5Sy2VNmzeslFSbH'
consumer_secret = 'PFKWP2bOkTudCWAnCnXuuW0zDRriTtjXI5cRRIVKuvJ62xz0kT'
access_token = '1140538463927898113-7KmKMN9Fcj763Ira01e4u88cmZ4Dfh'
access_token_secret = '2AY0AtaeuLMTvartFJg1uS7a2NKYM8vE7dPqaOODGsggE'

# Loging to the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Collecting the hashtag
getHashtag()

#### Restart the script
while(restart):
    answer = input("Do you want to collect another tweet ? [y/N] ")
    answer = answer.strip().lower()
    if answer.startswith('y'):
        getHashtag()
    elif answer.startswith('n') or answer == '':
        print("Closed")
        restart = False
    else:
        print("Please answer by 'y' ou 'n'")