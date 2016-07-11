import tweepy


def get_twitter_feed(self)

    account = self.env['website.twitter_account'].search([])[0]

    
    if account:
        key = account.twitter_api_key
        secret = account.twitter_api_secret
        token = account.twitter_token
        token_secret = account.twitter_token_secret
 
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token, token_secret)
    client = tweepy.API(auth)
     
    # timeline = client.statuses.home_timeline()
    userposts = client.user_timeline(screen_name='Therp_BV')

    if userposts:
        for item in userposts:
            tweet_dict = {
                'tweet_id' : item['id'],
                'text': item['text']
                'author' item['user']
                }
            self.env['website.tweet'].create(tweet_dict)




    def cleanup_old_feed(self):
        pass
