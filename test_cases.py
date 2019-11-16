from parser import *

# Every given test case in prefix notation
ONE = Sequent([], [('or',('neg','p'),'p')])
TWO = Sequent([('neg',('or','p','q'))], [('neg','p')])
THREE = Sequent(['p'], [('imp','q','p')])
FOUR = Sequent(['p'], [('or','p','q')])
FIVE = Sequent([('and',('and','p','q'),'r')], [('and','p',('and','q','r'))])
SIX = Sequent([('iff','p','q')], [('neg',('iff','p',('neg','q')))])
SEVEN = Sequent([('iff','p','q')], [('imp',('iff','q','r'),('iff','p','r'))])
EIGHT = Sequent([], [('imp',('and',('neg','p'),('neg','q')),('iff','p','q'))])
NINE = Sequent([('iff','p','q')], [('or',('and','p','q'),('and',('neg','p'),('neg','q')))])
TEN = Sequent([('imp','p','q'), ('imp',('neg','r'),('neg','q'))], [('imp','p','r')])

TESTS = [ONE,
		TWO,
		THREE,
		FOUR,
		FIVE,
		SIX,
		SEVEN,
		EIGHT,
		NINE,
		TEN,]

def print_all():
	for t in tests:
		print(t)
