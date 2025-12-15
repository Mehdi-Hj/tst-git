def r():
    return False

def gn_counter(start, jump=1):
    counter = start
    while True:
        yield counter
        counter += jump
