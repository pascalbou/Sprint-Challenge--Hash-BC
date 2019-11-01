#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # following hints
    # store all weights in ht
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    # loop all weights and check if a value for limit - weight exists in ht
    for j in range(len(weights)):
        diff = limit - weights[j]
        diff_index = hash_table_retrieve(ht, diff)
        if diff_index:
            if j < diff_index:
                return diff_index, j
            else:
                return j, diff_index

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
