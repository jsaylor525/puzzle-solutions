def f1(lIn):
    l1 = sorted(lIn) #sort the list
    l2 = [i for i in l1 if i<0.5] #make a subset by comparing all values
    return [i*i for i in l2] #square smaller subset

#winner, always reduce the set of data to process beforehand, if you are going to
def f2(lIn):
    l1 = [i for i in lIn if i<0.5] #make a smaller list of values by value compare
    l2 = sorted(l1) #sort a subset (~%50) of the orginal list
    return [i*i for i in l2] #square sorted subset

def f3(lIn):
    l1 = [i*i for i in lIn] #square the whole set
    l2 = sorted(l1) #sort the whole set
    return [i for i in l1 if i<(0.5*0.5)] #reduce set

import cProfile
import random
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')
cProfile.run('f4(lIn)')