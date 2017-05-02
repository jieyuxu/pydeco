import time

def calcTime( fxn ):
	def inner( *arg ):
		orig = time.time()
		run = fxn(* arg)
		print "it took %s to execute" % (time.time()-orig)
		return run
	return inner

def getArgs( fxn ):
	def inner( *arg ): #* arg is the param passed into fxn
		print "the fxn name is %s, the arguments are %s" % (fxn.func_name, arg)
		return fxn(*arg)
	return inner

#just fxns to test

@calcTime
@getArgs
def fib(n):
	if n < 2:
		return n
	else:
		return fib( n-1 ) + fib( n-2 )

@calcTime
@getArgs
def sumTo(n):
	if n == 1:
		return n
	return n + sumTo(n-1)

print fib(3)
print sumTo(10)
