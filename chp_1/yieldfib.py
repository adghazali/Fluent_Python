def fib():
  a,b = 0,1
  while 1:
  	print b
  	yield b
  	a,b = b, b+a

fib()
