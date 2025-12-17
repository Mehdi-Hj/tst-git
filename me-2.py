def r():
    return False

def gn_counter(start, jump=1):
    counter = start
    while True:
        yield counter
        counter += jump

create_id = 0
import random
class OP:
    def __init__(self):
        self.id = create_id
        create_id += random.randint(1, 100) 
