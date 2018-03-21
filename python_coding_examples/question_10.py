class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards


print("a.go()")
a.go()
print("b.go()")
b.go()
print("c.go()")
c.go()
print("d.go()")
d.go()
print("e.go()")
e.go()

print("a.stop()")
a.stop()
print("b.stop()")
b.stop()
print("c.stop()")
c.stop()
print("d.stop()")
d.stop()
print("e.stop()")
e.stop()

try:
    print("a.pause()")
    a.pause()
except:
    print("Exception!")
    pass
try:
    print("b.pause()")
    b.pause()
except:
    print("Exception!")
    pass
try:
    print("c.pause()")
    c.pause()
except:
    print("Exception!")
    pass
try:
    print("d.pause()")
    d.pause()
except:
    print("Exception!")
    pass
try:
    print("e.pause()")
    e.pause()
except:
    print("Exception!")
    pass