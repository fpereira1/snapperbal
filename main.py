import sys
import getpass
import prettytable
import optparse

from snapper import *

def main():
	print "To use this tool you must have your cards registered at %s" % ('www.snapper.co.nz')

	p = optparse.OptionParser()
	p.add_option('--email', '-e')
	options, arguments = p.parse_args()
	if options.email:
		email = options.email
	else:
		email = raw_input("Email: ")
	passwd = getpass.getpass("Password: ")

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

if __name__ == "__main__":
    main()


