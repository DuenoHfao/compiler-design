r1 = [0,0,0,0,0,0,0,1] #+
r2 = [0,0,0,0,1,1,0,1] #1 + 4 + 8 = 13
r3 = [0,0,0,0,1,0,0,0] #8
c1 = [0,0,0,0,0,0,0,0] #cpu cache 1
c2 = [0,0,0,0,0,0,0,0] #cpu cache 2

'''
Sends x84 ISA to cpu

r2 is at ram loc 0010
r3 is at ram loc 0011

00000001|0010|0011|
which tranlates to
r2 = r2 + r3

*UNKNOWN*
CPU takes in ISA
Binary Numbers --> Electrical Signal Instructions (HOW)

DOES OPERATION (SEE BELOW)

STORE IN RAM (PHYSICAL CHANGE OF STATE)
'''

i = 7 #COUNTER should not exist in CPU, proccesses are done without any storage in cpu except for cache usage

def XOR(i1, i2):
    return int(bool(i1) ^ bool(i2))

def AND(i1, i2):
    return int(bool(i1) and bool(i2))

def OR(i1, i2):
    return int(bool(i1) or bool(i2))

while i >= 0:
    #print(r2[i], r3[i], c2[-1])
    c1[-1] = OR(AND(r2[i], r3[i]), AND(r3[i], c2[-1]))
    r2[i] = XOR(XOR(r2[i], r3[i]), c2[-1])
    c2[-1] = c1[-1]
    #print(r2[i], c2[-1])
    i -= 1
    
print(r2)