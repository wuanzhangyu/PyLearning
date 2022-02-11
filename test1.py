def runlengthencode(t):
    count = 0       # how often did we see this character?
    cha = t[0]    # which character
    rv = []       # resulting list that stores our (character, count) tuples
    for c in t:   # process each character of the given text
        if c == cha:  # if it is equal to what we look for
            count += 1       # increment counter
        else:
            rv.append((cha, count))
            count = 1       # append so far counted ones as tuple (character,count)
            cha = c       # and remember the new char with a count of 1

    rv.append((cha, count))   # add the last character and its count

    # produce the output from our remembered tuples
    # return ' '.join("{} {}".format(charac, nr) for charac, nr in rv)
    return ' '.join("[{} {}]".format(charac, nr) for charac, nr in rv)


text = "0"


print(runlengthencode(text))