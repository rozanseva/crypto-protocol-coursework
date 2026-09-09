import random
import time

def randomBitGenerator(wlen: int):
    w = 0
    for i in range(0,wlen):
        w = w << 1 | random.randint(0,1)
    return w

def generate_random_number(start, end):
    current_time = int(time.time())
    seed = current_time % (end - start + 1)
    return start + seed

def millerRabin(w, iterations):
    if w % 2 == 0:
        return False
    m = w - 1
    a = 0
    while m % 2 == 0:
        m = m >> 1
        a += 1
    wlen = w.bit_length()
    for i in range(iterations):
        b = 0
        while b < 1 or b >= w - 1:
            b = randomBitGenerator(wlen)
        z = pow(b, m, w)
        if z == 1 or z == w - 1:
            continue
        for j in range(a - 1):
            z = pow(z, 2, w)
            if z == w - 1:
                break
            if z == 1:
                return False
        if z != w - 1:
            return False
    return True

def get_prime(a : int):
    while True:
        w = randomBitGenerator(a)
        if millerRabin(w,40) :
            break
    return w 

def get_prime_(a,b):
    while True:
        w = generate_random_number(a,b)
        if millerRabin(w,40) :
            break
    return w 


#def is_prime1(w):
    #k = 0
    #for i in range(2, int(w ** 0.5) + 2):
        #if w % i == 0:
            #k = k + 1
            #break
    #if k <= 0:
        #return True
    #else:
        #return False
#w = 11796339313185253243
#print (w,is_prime1(w))



#def is_prime(num, test_count):
    #for i in range(test_count):

        #rnd = random.randint(1, num - 1)

        #if (rnd ** (num - 1) % num != 1):
            #return False

    #return True