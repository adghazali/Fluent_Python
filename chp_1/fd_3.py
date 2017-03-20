import collections 
import inspect 

x = collections.namedtuple('Card', 'rank suit', #verbose = True)
												)

## class Card(tuple) is a subclass of tuple 
print(inspect.getmro(x) )