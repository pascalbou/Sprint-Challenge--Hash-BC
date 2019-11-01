#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # store all tickets in hashtable
    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # initialize starting point
    src = 'NONE'
    dest = ''
    index = 0

    # from start save the next destination to route
    while dest != 'NONE':
        dest = hash_table_retrieve(hashtable, src)
        route[index] = dest
        src = dest
        index += 1

    return route
