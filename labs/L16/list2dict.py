def list2dict(lst):
    # Traditional loop construction
    # dictionary = dict()
    # for i, item in enumerate(lst, 1):
    #     dictionary[i] = item
    # return dictionary
    return {i: item for i, item in enumerate(lst, 1)}
