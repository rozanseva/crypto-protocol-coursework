import time
from threading import Thread
import random

def generate_q_with_time():
    global q
    while True:
        timestamp = int(time.time())
        q = timestamp - (timestamp//137)
        return q

def generate_random_q():
    global r
    while True:
        r = random.randint(0, 2**160)
        decimal_number = int("".join(str(x) for x in bin(r)[2:]), 2)
        if 159<=decimal_number<=160:
            return decimal_number
        else:
            r = random.randint(0, 2**160)
            decimal_number = int("".join(str(x) for x in bin(r)[2:]), 2)

def is_prime1(number):
    k = 0
    for i in range(2, int(number ** 0.5) + 2):
        if number % i == 0:
            k = k + 1
            break
    if k <= 0:
        return True
    else:
        return False

def main():  
    t1 = Thread(target=generate_q_with_time) 
    t2 = Thread(target=generate_random_q)

    t1.start()
    t2.start()  

    while t1.is_alive() or t2.is_alive():
        try:
            q = t1.join().result()
            return q
            #print_q(q)    
        except Exception as e:
            pass
        try:
            r = t2.join().result()
            return r
            #print_q(r) 
        except:
            pass  




# import datetime


# def gen(left=1, right=2**128):
#     if not hasattr(gen, 'N'):
#         gen.N = datetime.datetime.now().microsecond
#     gen.N = (5 ** 76 * gen.N) % (2 ** 160)
#     out = int(str(gen.N * 1.0 / (2 ** 160))[2:]) % right
#     if out > left:
#         return out
#     else:
#         return gen(left, right)


# def is_prime1(number):
#     k = 0
#     for i in range(2, int(number ** 0.5) + 2):
#         if number % i == 0:
#             k = k + 1
#             break
#     if k <= 0:
#         return True
#     else:
#         return False


# def is_prime2(number):
#     for _ in range(20):
#         n = gen(right=number - 1)
#         if pow(n, number - 1, number) != 1:
#             return False
#         return True


# def gen_prime(left=1, right=2 ** 128):
#     while True:
#         rand_num = gen() % right
#         if rand_num > left:
#             if is_prime1(rand_num) and is_prime2(rand_num):
#                 return rand_num
#             else:
#                 continue
#         else:
#             gen_prime(left, right)

# for i in range(20):
#     try:
#         print(gen_prime(right=10000000000))
#     except ZeroDivisionError:
#         pass
