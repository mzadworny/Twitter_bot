import twitter

api = twitter.Api(consumer_key='-',
                  consumer_secret='-',
                  access_token_key='-',
                  access_token_secret='-')

status = api.PostUpdate('Ten post został utworzony za pomocą aplikacji napisanej w języku Python!')
print(status.text)

#testuje git
#no to teraz kolejny test