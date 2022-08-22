import FAQbot
import APIbot
import JOINbot
from keep_alive import keep_alive
import asyncio



if __name__ == "__main__":
  keep_alive()
  loop = asyncio.get_event_loop()
  coros = []
  coros.append(FAQbot.bot.polling())
  coros.append(APIbot.bot.polling())
  coros.append(JOINbot.bot.polling())
  loop.run_until_complete(asyncio.gather(*coros))