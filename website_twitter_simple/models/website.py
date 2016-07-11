# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
import tweepy



class Website(models.Model):
    """ when making it multi website
    _name = 'twitter.simple.config.settings'
    _inherit = 'website.config.settings'
    """
    _inherit = 'website'

    twitter_api_key = fields.Char(
        string='Twitter API Key',
	help="Twitter API key you can get it from https://apps.twitter.com/app/new"
    )
    twitter_api_secret = fields.Char(
	string='Twitter API secret',
	help="Twitter API secret you can get it from https://apps.twitter.com/app/new"
    )
    
    twitter_token = fields.Char(
        string='Token for twitter application',
        help="Create a new application from apps.twitter.com"
             "then generate the token and paste it here" )


    twitter_token_secret = fields.Char(
        string='Token secret for twitter application',
        help="Create a new application from apps.twitter.com"
             "then generate the token secret and paste it here"     )
    twitter_screen_name = fields.Char(
	string='Get favorites from this screen name',
	help="Screen Name of the Twitter Account from which you want to load favorites."
	"It does not have to match the API Key/Secret."
    )
  
    feed_length = fields.Integer('Number of tweets to show on the website')

    @api.model
    def get_twitter_feed(self):

        account = self.env['website'].search([])     
        if account[0].twitter_api_key:
            #monowebsite mono config
            key = account[0].twitter_api_key
            secret = account[0].twitter_api_secret
            token = account[0].twitter_token
            token_secret = account[0].twitter_token_secret

        auth = tweepy.OAuthHandler(key, secret)
        auth.set_access_token(token, token_secret)
        client = tweepy.API(auth)
         
        # timeline = client.statuses.home_timeline()
        userposts = client.user_timeline()

        if userposts:
            for item in userposts:
                tweet_dict = {
                    'text': item.text,
                    'author_name': item.author.name,
                    'author_screen_name': item.author.screen_name,
                    'tweet_create_date': item.created_at,
                    'tweet_id' : item.id,
                    }
                self.env['website.tweet'].create(tweet_dict)
                for entity in item.entities['user_mentions']:
                    entitydict = {
                        'twitter_user_id' : entity['id'],   
                        'twitter_user_name': entity['name'],
                        'twitter_user_screen_name' : entity['screen_name'],
                        'mentions':1
                        }
                    exists = self.env['twitter.user'].search(
                        [('twitter_user_id', '=', entity['id'])])
                    if exists:
                        exists[0].write({'mentions': exists.mentions +1})
                    else:
                        self.env['twitter.user'].create(entitydict)




    def cleanup_old_feed(self):
        pass
