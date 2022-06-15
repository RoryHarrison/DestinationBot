from discord.ext import commands, tasks
from datetime import datetime
import pytz

class NotifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.notify.start()

    def cog_unload(self):
        self.notify.cancel()

    @tasks.loop(minutes=1)
    async def notify(self):
        tz_seoul = pytz.timezone('Asia/Seoul')
        datetime_seoul = datetime.now(tz_seoul)
        seoul_time = datetime_seoul.strftime("%H:%M")

        hot_time = "01:35"
        reset_time = "00:00"

        if seoul_time == hot_time:
            print("Sending Hot Time Message")
            try:
                channel = self.bot.get_channel(984516754837491882)
                await channel.send('<@&986669663909986365> Hot Time :fire:')
            except Exception as e:
                print(f"failed to send message: {e}")


        if seoul_time == reset_time:
            print("Sending Reset Time Message")
            try:
                channel = self.bot.get_channel(984516754837491882)
                await channel.send('<@&986669663909986365> Reset Time :recycle:')
            except Exception as e:
                print(f"failed to send message: {e}")


    @notify.before_loop
    async def before_notify(self):
        print('waiting...')
        await self.bot.wait_until_ready()
        
def setup(bot):
    bot.add_cog(NotifyCog(bot))
    print("Notify Loaded")