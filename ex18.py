# this one is like your scripts with argv

def print_two (*args):
	arg1, arg2 = args
	print "%r %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
		print "%r %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "%r" % arg1

def print_none():
	print "I got nothing"

print_two("Fritz","Brooks")
print_two_again("Fritz", "Brooks")
print_one("First!")
print_none()
