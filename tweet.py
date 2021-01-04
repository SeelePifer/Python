import twitter
import random
#Get Twitter followers
api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
print(api.VerifyCredentials())
followers = api.GetFollowers()

randomIndex=random.randint(0,len(followers)-1)
randomFollower= followers[randomIndex]
print(randomFollower.screen_name)

tweet = "@{} you are a random follower of the day.TURN UP!".format(randomFollower.screen_name)
api.PostUpdate("I love Python-twitter!")
print(tweet)
print("Thanks for tweeting")
