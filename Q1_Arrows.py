import sys
import collections
def solutions(S):
    sorted_dict = {}
    list1=collections.Counter(S)
    sorted_keys = sorted(list1, key=list1.get)
    for w in sorted_keys:
        sorted_dict[w] = list1[w]
    first_value = list(sorted_dict.items())[0][1]
    op = sum(sorted_dict.values())
    Result = op-first_value
    print ('The arrows to be rotated to make all are in same direction: ',Result)
    return Result
if __name__ == "__main__":
    S = "<<<"
    print (solutions(S))