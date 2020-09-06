#twitter bot
import tweepy
import os
def create_api():
  consumer_key=os.getesv('consumer_key')
  consumer_secret=os.getesv('consumer_secret')
  access_token=os.getesv('access_token')
  access_token_secret=os.getesv('access_token_secret')
  auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_token,access_token_secret)
  api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  return api 

#complete code
import time
def follower_count(user):
  emoji_numbers={0:'0️⃣ ',
                1:'1️⃣ ',
                2:'2️⃣ ',
                3:'3️⃣ ',
                4:'4️⃣ ',
                5:'5️⃣ ',
                6:'6️⃣ ',
                7:'7️⃣ ',
                8:'8️⃣ ',
                9:'9️⃣  '}
                
  uf_split=[int(i) for i in str(user.followers_count)]#list comprenhension

  user_emoji=''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
  return(user_emoji)
def main():
  api=create_api()
  while True:
    user=api.get_user('PillySimha')
    api.update_profile(name=f'simha|{follower_count(user)}followers')
    print(f'updating name:{follower_count(user)}')
    time.sleep(60)
    print('waited for refresh')
main()
