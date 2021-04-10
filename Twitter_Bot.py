import twitter

#You can add your access tokens from Twitter.

api = twitter.Api(consumer_key='-',
                  consumer_secret='-',
                  access_token_key='-',
                  access_token_secret='-')

status = api.PostUpdate('Ten post został utworzony za pomocą aplikacji napisanej w języku Python!')
print(status.text)

#Executing this file after providing your access tokens will push the string as your status update on Twitter!

#Now it works?
#Test

