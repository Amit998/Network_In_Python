from instabot import Bot


bot=Bot()

bot.login(username="iam_amit98",password='')

# bot.upload('test.jpg',caption='Baby Yoda')
# bot.follow('elonofficiall')
# bot.send_message('Hi Doba',['bee._.in_my_bonnet'])

followers=bot.get_user_followers("elonofficiall")

print(followers)