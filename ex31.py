print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "Theres a giant bear eating cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Yell at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    if bear == "2":
        print "The bear tears your leg off. Good job1"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow Jacket Clothespins"
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input ("> ")

    if insanity == "1" or  insanity == "2":
        print "Your body survives powered by the mind of jello. Good job!"
    else:
        print "The insanity rots your eyes out into a pool of muck. Good job!"

else:
    print "You stumbled around and fall into a knife and die. Good job!"
