def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2 %r" % (arg1, arg2)
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_one(arg):
	print "arg: %r" % (arg)
def print_none():
	print "This takes no arg lol"

print_two("Fritz", "Brooks")
print_two_again("Fritz", "Brooks")
print_one("Fritz")
print_none()