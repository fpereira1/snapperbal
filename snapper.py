import urllib, urllib2
import locale
from cookielib import CookieJar
from BeautifulSoup import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'en_NZ.UTF-8')

class SnapperAccount:

	base = "https://www.snapper.co.nz/"

	def __init__(self, email, passwd):

		self.user    = {}
		self.cards   = []

		params = {
			'Email'    : email,
			'Password' : passwd,
			'Remember' : 1,
			'AuthenticationMethod' : "MemberAuthenticator",
			'BackURL'  : "/my-account/"
		}

		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
		params = urllib.urlencode(params)

		# Send request to snapper to login via HTTPs
		response = opener.open(SnapperAccount.base+"home/LoginForm/", params)

		# Start the soup object where we can query dta from HTML
		soup = BeautifulSoup(response)

		# Greetings
		user = str(soup.h1.renderContents())
		if 'Welcome' in user:
			self.user = user.split(',')[1].strip()

		cards = soup.findAll('div', { 'class': 'cardText' })

		for card in cards:
			cardname = card.h2.a.renderContents()
			amount   = card.find('span', {'class':'completeValue'}).renderContents()
			self.cards.append(SnapperCard(cardname, float(amount)))
		
	


class SnapperCard:
	def __init__(self, title, amount):
		self.title  = title
		self.amount = float(amount)

	def amount_display(self):
		return locale.currency(self.amount, grouping=True)

	def to_array(self):
		return [self.title, self.amount_display()]