from instagram_follow_bot import InstagramFollowerBot
import os

#your login credentials and driver path
INSTAGRAM_ACCOUNT = os.getenv("INSTAGRAM_ACCOUNT")  #your Twitter account
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")  #your password
DRIVER_PATH = os.getenv('DRIVER_PATH')  #your driver path

#using bot to log in
bot = InstagramFollowerBot(driver_path=DRIVER_PATH)
bot.login(instagram_account=INSTAGRAM_ACCOUNT, instagram_password=INSTAGRAM_PASSWORD)

#pulls up similar instagram account
similar_account = "chefsteps"
bot.find_followers(similar_account_name=similar_account)
bot.follow()

