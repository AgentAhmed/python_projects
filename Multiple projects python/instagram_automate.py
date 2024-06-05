from instabot import Instabot

bot = Bot()
bot.login(username="abc",password="***")
# bot.follow("wscubetechindia")

# bot.upload_photo("path",caption="")
# bot.unfollow("wscubetechind")

# bot.send_message("abasfdhhdfghfi",["aru","baru","kolu","etc"])

# followers = bot.get_user_followers("abc")
# for follower in followers:
#     print(bot.get_user_info(follower))
    
following = bot.get_user_followers("abc")
for Following in following:
    print(bot.get_user_info(following))    