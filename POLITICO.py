import requests
from bs4 import BeautifulSoup
import telegram
import schedule
import time
from telegram import ParseMode

channel = "@POLITICOnewsletter"

# Change headers otherwise Politico bounces me back with 403 forbidden
headers = {'User-Agent': 'Mozilla/5.0'}

# Brussels playbook parser



message = ""
url = "https://www.politico.eu/newsletter/brussels-playbook"
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("h2")

# Using stop character to break out of loops after first link which 
# *should* be current newsletter
stop = 0
for link in links:
	title = link.get("class")
	if stop == 0:
		if str(title) == "['card__title']":
			testo = link.find("a")
			message= testo.get("href")
			stop += 1

brux = "[Brussels playbook](" + message + ")"
###

# Morning tech parser
message1 = ""
url = "https://www.politico.com/newsletters/morning-tech"
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("h3")
stop = 0
for link in links:
	if stop == 0:
		testo = link.find("a")
		message1 = testo.get("href")
		stop += 1

morning = "[Morning tech](" + message1 + ")"
#####



my_token = "TOKEN"

def send(msg, chat_id, token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg, parse_mode="MarkdownV2")
	#parse_mode gives me the ability to use markdown syntax to format the links


schedule.every().day.at("8:00").do(push)

while 1:
    schedule.run_pending()
    time.sleep(1)

