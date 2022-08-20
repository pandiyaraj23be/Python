import sys
import os
import collections
def solutions(S):
    x=3
    val=0
    res=[S[y-x:y] for y in range(x, len(S)+x,x)]
    #print res
    for i in res:
        for j in i:
            if j=="X":
                val=val+1
                break
            else:
                print "fail"
        #print val
    print ("Min. no. patches required: ",val)
    return val
if __name__ == "__main__":
    S = "XXXX"
    print(solutions(S))