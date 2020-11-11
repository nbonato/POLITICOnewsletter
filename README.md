# POLITICOnewsletter
Unofficial bot for keeping up with POLITICO's newsletters

## Introduction

Bot created using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
Every day at 8:00 UTC the bot navigates to Politico's [Morning Tech](https://www.politico.com/morningtech/) and [Brussels Playbook](https://www.politico.eu/newsletter/brussels-playbook/) newsletters' pages. It retrieves the latest issue and sends the link to the [@POLITICOnewsletter](https://t.me/POLITICOnewsletter) Telegram Channel, where it can be read using the Instant View feature. 

Morning Tech gets published at 10:00 EST, so the issue that appears on the channel has been published the day before at 15:00 UTC.

Brussels Playbook gets published around 7:00 UTC+1 (Brussels timezone), so the issue that appears on the channel appears on the same day, some two hours later.

## Libraries and modules used
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for creating and operating the bot
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](https://requests.readthedocs.io/en/master/) for scraping the newsletters' pages and getting the latest issue
* [datetime](https://docs.python.org/3/library/datetime.html) and [threading](https://docs.python.org/3/library/threading.html) to send the messages every day at the same time
