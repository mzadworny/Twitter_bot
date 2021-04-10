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
<<<<<<< HEAD
#Test
=======
#Last one
>>>>>>> 04579010f8433216bac39ad43e3ea114f2e96bd5

