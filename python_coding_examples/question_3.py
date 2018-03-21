#!/usr/bin/python

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print("list(zip(={}".format(list(zip(('a','b','c','d','e'),(1,2,3,4,5)))))

print("A2 = sorted([i for i in A1 if i in A0]):\n\t",end='')
for i in A1:
    if i in A0:
        print(i, A0[i], end='')
print("")

print("A3 = sorted([A0[s] for s in A0])\n\t",end='')
for s in A0:
    print("A0[{}]={} ".format(s, A0[s]), end='')
print("")

print("A4 = [i for i in A1 if i in A3]\n\t",end='')
for i in A1:
    print("{} ".format(i), end='')
    # if i in A3:
        # print("A3[{}]={} ".format(i, A3[i]), end='')
print("")

print("A5 = {i:i*i for i in A1}\n\t",end='')
for i in A1:
    # print("{}:".format(i), end='')
    # print("{} ".format(i*i),end='')
    print("A5[{}]={} ".format(i, A5[i]), end='')
print("")

print("A6 = [[i,i*i] for i in A1]\n\t",end='')
for i in A1:
    # print("{}:".format(i), end='')
    # print("{} ".format(i*i),end='')
    print("A6[{}]={} ".format(i, A6[i]), end='')
print("")

print("A0 = {}".format(A0))
print("A1 = {}".format(A1))
print("A2 = {}".format(A2))
print("A3 = {}".format(A3))
print("A4 = {}".format(A4))
print("A5 = {}".format(A5))
print("A6 = {}".format(A6))