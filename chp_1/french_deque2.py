import collections 

Card = collections.namedtuple('Card','rank suit', verbose = True)   ##factory function for creating a subclass of tuple named arg1 , with attributes of arg2
## this creates a new tuple subclass named 'Card' with the attributes 'rank' and 'suit'
## we bind it to the variable Card so that it points to the subclass of hte same name
## and we can assign using Card(rank,suit)

class FrenchDeck:
	ranks = [str(i) for i in range(2,11)]+ list('JQKA')	
	suits = 'spades hearts diamonds clubs'.split()
	
	def __init__(self):   ## you must define the initial state of instance attributes 
	    		## we have to refer to instance variable as self.cards
		self.cards = [Card(rank,suit) for rank in self.ranks  ## we have to pass in self which refers to own class to get class variables
				  					  for suit in self.suits ]

	def __len__(self):
		return len(self.cards)

	def __-__*(self):
		


deck = FrenchDeck()
print(len(deck))
