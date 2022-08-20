import sys
import os
import collections
def solution(S):
    if len(S) == 1:
        return -1
    count = 0
    last_index = len(S)
    for index in range(len(S)):
        P_Value = False
        N_Value = False

        if S[index] == "H":
            if index != 0 and S[index-1] == '-':
                P_Value = True
            if index != len(S) - 1 and S[index+1] == '-':
                N_Value = True

            if not (P_Value or N_Value):
                return -1
            # do we have - in prev or next
            if N_Value and (index - 1 != last_index or not P_Value):
                count += 1
                last_index = index + 1
            if P_Value and not N_Value and last_index != index - 1:
                count += 1
                last_index = index - 1
    return count


if __name__ == "__main__":
    S = '-H-H-H-H-H'
    print(solution(S))