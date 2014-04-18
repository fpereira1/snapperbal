import sys
import getpass
import prettytable
import optparse
import locale
import urllib, urllib2
from cookielib import CookieJar
from BeautifulSoup import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'en_NZ.UTF-8')

__version__ = '1.1.1'

def main():

    p = optparse.OptionParser(usage="%prog [-e]", version="%prog "+__version__)
    p.add_option('--email', '-e')
    options, arguments = p.parse_args()

    if options.email:
        email = options.email
    else:
        email = raw_input("Email: ")
    passwd = getpass.getpass("Password: ")

    print "To use this tool you must have your cards registered at %s" % ('www.snapper.co.nz')
    print '\033[91m' + "Looking for your Snapper balance..." + '\033[0m'
    print "Your balance may be different from the actual Snapper balance"

    s = SnapperAccount(email, passwd)

    if not len(s.cards):
        print "I am sorry. No data has been found. Have you got a snapper account?"
    else:
        tb = prettytable.PrettyTable(['Card', 'Amount'])
        for l in s.cards:
            tb.align['Card'] = 'l'
            tb.align['Amount'] = 'r'
            tb.add_row(l.to_array())

        print """
Hi %s,

We've found your details! Here is your balance:

%s""" % (s.user, tb)



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


if __name__ == "__main__":
    main()

