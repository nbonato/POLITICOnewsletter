import requests
from bs4 import BeautifulSoup
import telegram
import schedule
import time
from telegram import ParseMode
from boto.s3.connection import S3Connection

channel = "@POLITICOnewsletter"

# Change headers otherwise Politico bounces me back with 403 forbidden
headers = {'User-Agent': 'Mozilla/5.0'}

# Brussels playbook parser

url1 = "https://www.politico.eu/newsletter/brussels-playbook"
url2 = "https://www.politico.com/newsletters/morning-tech"

def parse(address, level, linktxt=None, titletxt=None):	
	message = ""
	response = requests.get(address, headers=headers)
	html = response.text

	soup = BeautifulSoup(html, "html.parser")
	links = soup.findAll(level)
	# Using stop character to break out of loops after first link which 
	# *should* be current newsletter
	stop = 0
	for link in links:
		title = link.get(linktxt)
		if stop == 0:
			if titletxt is not None and str(title) == titletxt:
				testo = link.find("a")
				message= testo.get("href")
				stop += 1
			else:
				testo = link.find("a")
				message= testo.get("href")
				stop += 1
	return(message)

brux = "[Brussels playbook](" + parse(url1, "h2", "class", "['card__title']") + ")"
morning = "[Morning tech](" + parse(url2, "h3") + ")"


#my_token = 'TOKEN'

def send(msg, chat_id, token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg, parse_mode="MarkdownV2")
	#parse_mode gives me the ability to use markdown syntax to format the links


send(brux, channel, my_token)
send(morning, channel, my_token)


def push():
	send(brux, channel, my_token)
	send(morning, channel, my_token)

schedule.every().day.at("07:30").do(push)

while 1:
    schedule.run_pending()
    time.sleep(1)
