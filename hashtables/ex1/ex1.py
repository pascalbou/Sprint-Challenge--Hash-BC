#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # BAD algorithm
    # sort the weights
    # loop start from highest
    # while high + number not equal to limit
        # if high + number > limit
            # break the loop
        # number increment
    # return 0=high, 1=number

    # following hints
    # store in ht
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(weights)):
        

    for i in range(len(weights), -1):
        print(weights[i])

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
