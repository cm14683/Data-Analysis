#imports
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


#For Percentage calculation
def percentage(part, whole):
	return 100*float(part)/float(whole)

#Twitter Personal Details
consumerKey = "";
consumerSecret = "";
accessToken = "";
accessTokenSecret = "";

#Authorization
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


#Personalised Text entry for users and no. of tweets u want to search
searchTerm = raw_input("Enter the Keyword/Hashtag to search: ")
noOfSearchTerms = int(input("Enter how many tweets to analyse: "));

#Setting the Cursor for searching the user input in given no. of tweets specified
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)


#Storing the polarity
positive = 0
negative = 0
neutral = 0

#For average sentiment of tweets
polarity = 0

for tweet in tweets:
	print(tweet.text)	
	
	analysis = TextBlob(tweet.text)
	polarity += analysis.sentiment.polarity
	
	if(analysis.sentiment.polarity == 0):
		neutral +=1

	elif(analysis.sentiment.polarity < 0.00):
		negative +=1

	elif(analysis.sentiment.polarity > 0.00):
		positive +=1


#Calculation of Percentage
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

#The results fetched above may be upto 6-7 decimal places, So rounding upto 2 decimal places
positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
polarity = format(polarity, '.2f')

#Printing the Analysed report
print("How people are reacting on " + searchTerm + " by analysing " + str(noOfSearchTerms) + " Tweets.")


if(polarity == 0):
	print("Neutral")

elif(polarity < 0.00):
	print("Negative")

elif(polarity > 0.00):
	print("Positive")


#Plotting on Matplotlib
labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 'Neutral ['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['yellow', 'gold', 'red']
patches, text = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on " + searchTerm + " by analysing " + str(noOfSearchTerms) + " Tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()






