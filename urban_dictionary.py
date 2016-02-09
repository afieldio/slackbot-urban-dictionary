import urllib2
from lxml import html
import requests
import json


page = requests.get('http://www.urbandictionary.com/random.php')
tree = html.fromstring(page.content)

word = tree.xpath('//a[@class="word"]/text()')
meaning = tree.xpath('//div[@class="meaning"]/text()')
example = tree.xpath('//div[@class="example"]/text()')

if ' ' in word[0]:
	for l in word[0]:
	 	word[0].replace(' ', '\\')

url = 'Enter Slack Webhook URL here'
payload = {'text': '<http://www.urbandictionary.com/define.php?term={0} | *Word of the day*: {0}> \n *Meaning:* {1} \n *Example:* {2}'.format(word[0], meaning[0], example[0]), 'username':'Urban Dictionary', 'icon_emoji': ':troll:'}
headers = {'content-type': 'application/json'}


response = requests.post(url, data=json.dumps(payload), headers=headers)