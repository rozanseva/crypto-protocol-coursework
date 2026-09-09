from prandom import *
from prime import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import math as m

def Posrednik():
    global window_p
    global tree_p
    global btn_keys
    global btn_send_open
    global btn_send_close
    window_p = Tk()
    window_p.title("Посредник")
    window_p.geometry("400x500")
    window_p.configure(bg='salmon')
    columns_p = ("p")
    tree_p = ttk.Treeview(window_p, columns=columns_p, show="headings")
    tree_p.pack(fill=BOTH, expand=1)
    tree_p.heading("p", text="Посредник:", anchor=W)
    style = ttk.Style(window_p)
    style.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["p =", "q =", "n =", "v =", "v-1 =", "s ="]
    for i in data:
        tree_p.insert("", END, values=i)
    btn_pq = ttk.Button(window_p, text="1. Генерация p и q", command=click_pq)
    btn_pq.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_keys = ttk.Button(window_p, text="2. Генерация ключей", command=click_keys, state=["disabled"])
    btn_keys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_open = ttk.Button(window_p, text="3. Публикация открытого ключа", command=click_send_keys_open, state=["disabled"])
    btn_send_open.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_close = ttk.Button(window_p, text="4. Передача закрытого ключа", command=click_send_keys_close, state=["disabled"])
    btn_send_close.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    window_p.mainloop()

def Prime():
    global window_prime, entry, label1
    window_prime = Tk()
    window_prime.title("Проверка числа на простоту")
    window_prime.geometry("400x200")
    window_prime.configure(bg='salmon')
    label = ttk.Label(window_prime, text="Введите число для проверки", font=("Times New Roman", 16))
    label.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    entry = ttk.Entry(window_prime)
    entry.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    miller_checkbutton = ttk.Button(window_prime, text="Тест Миллера — Рабина", command=prime_n)
    miller_checkbutton.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    is_prime1_checkbutton = ttk.Button(window_prime, text="Тест пробных делений", command=prime_n2)
    is_prime1_checkbutton.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    label1 = ttk.Label(window_prime, text="", font=("Times New Roman", 16))
    label1.pack(fill=X, padx=[5,5], pady=5, side=TOP)

def prime_n():
    global t
    t = entry.get()
    t = int(t)
    if millerRabin(t,40):
        label1["text"] = "Число является простым"
    else:
        label1["text"] = "Число не является простым"


def prime_n2():
    global t
    t = entry.get()
    t = int(t)
    if is_prime1(t):
        label1["text"] = "Число является простым"
    else:
        label1["text"] = "Число не является простым"


def A():
    global window_a
    global tree_a
    global btn_z, btn_send_z, btn_send_r, btn_y, btn_send_y
    window_a = Tk()
    window_a.title("А")
    window_a.geometry("400x500")
    columns_a = ("a")
    tree_a = ttk.Treeview(window_a, columns=columns_a, show="headings")
    tree_a.pack(fill=BOTH, expand=1)
    tree_a.heading("a", text="А:", anchor=W)
    style_1 = ttk.Style(window_a)
    style_1.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["n =", "v =", "s =", "r =", "z =", "b =", "y ="]
    for i in data:
        tree_a.insert("", END, values=i)
    btn_z = ttk.Button(window_a, text="5. Вычисление z", command=gen_z, state=["disabled"])
    btn_z.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_z = ttk.Button(window_a, text="6. Передача z", command=send_z, state=["disabled"])
    btn_send_z.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_r = ttk.Button(window_a, text="9. Передача r", command=send_r, state=["disabled"])
    btn_send_r.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_y = ttk.Button(window_a, text="9. Вычисление y", command=gen_y, state=["disabled"])
    btn_y.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_y = ttk.Button(window_a, text="10. Передача y", command=send_y, state=["disabled"])
    btn_send_y.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    
def B():
    global window_b
    global tree_b, btn_b, btn_send_b, btn_z_b, btn_y_b
    window_b = Tk()
    window_b.title("Б")
    window_b.geometry("400x500")
    columns_b = ("b")
    tree_b = ttk.Treeview(window_b, columns=columns_b, show="headings")
    tree_b.pack(fill=BOTH, expand=1)
    tree_b.heading("b", text="Б:", anchor=W)
    style_2 = ttk.Style(window_b)
    style_2.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["n =", "v =", "z =", "b =", "r =", "y ="]
    for i in data:
        tree_b.insert("", END, values=i)
    btn_b = ttk.Button(window_b, text="7. Генерация b", command=gen_b, state=["disabled"])
    btn_b.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_send_b = ttk.Button(window_b, text="8. Передача b", command=send_b, state=["disabled"])
    btn_send_b.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_z_b = ttk.Button(window_b, text="10. Проверка по r", command=z_b, state=["disabled"])
    btn_z_b.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_y_b = ttk.Button(window_b, text="11. Проверка по y", command=y_b, state=["disabled"])
    btn_y_b.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x_prev, y_prev = extended_gcd(b, a % b)
    x = y_prev
    y = x_prev - (a // b) * y_prev
    return gcd, x, y

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        #raise ValueError("Обратный элемент не существует")
        return -1
    else:
        return x % m

def click_pq():
    global p,q,k
    k = 14
    p = get_prime(k)
    q = get_prime(k)
    #p = get_prime_(2**(k-1), 2**k-1)
    #q = get_prime_(2**(k-1), 2**k-1)
    while (p % q == 0) or (q % p == 0):
        q = get_prime(k)
    global n
    n = p * q
    tree_p.set("I001", 0, "p = {}".format(p))
    tree_p.set("I002", 0, "q = {}".format(q))
    tree_p.set("I003", 0, "n = {}".format(n))
    btn_keys["state"] = "enabled"

def jacobi_symbol(a, n):
    if n == 1:
        return 1
    elif a == 0:
        if n % 2 == 1:
            return 0
        else:
            return 1
    elif a % 2 == 0:
        return jacobi_symbol(a // 2, n) if (n**2 - 1) % 8 == 0 or (n**2 - 1) % 8 == 7 else -jacobi_symbol(a // 2, n)
    else:
        return jacobi_symbol(n % a, a) if a % 4 == 3 and n % 4 == 3 else -jacobi_symbol(n % a, a)

def is_quadratic_residue(a, p):
    return jacobi_symbol(a, p) == 1

def click_keys():
    global v
    global v_1
    global s
    for i in range(2**(k-2), 2**k - 1):
        v = (i*i) % n
        if m.gcd(v,n)==1:
            v_1=pow(v,-1,n)
            break
        #v_1 = modular_inverse(v, n)
        #if (v_1 != -1):
            #break
        #if is_quadratic_residue(v, n):
            #v_1 = modular_inverse(v, n)
            #break
        #er = 1
        #for j in range(1, n-1):
            #if ((v * j) % n != 1):
                #continue
            #else:
                #er = 0 
                #v_1 = j 
                #break
        #if (er == 0):
            #break
        #else:
            #continue
    #for i in range(0, n):
        #p = i*n + v_1
        #if is_perfect_square(p):
            #s = int(p**0.5)
            #break
    for i in range(1, n):
        if ((i * i) % n == v_1):
            s = i
            break
    tree_p.set("I004", 0, "v = {}".format(v))
    tree_p.set("I005", 0, "v-1 = {}".format(v_1))
    tree_p.set("I006", 0, "s = {}".format(s))
    btn_send_open["state"] = "enabled"

def is_perfect_square(number):
    sqrt = int(number ** 0.5)
    return sqrt * sqrt == number


def click_send_keys_open():
    tree_a.set("I001", 0, "n = {}".format(n))
    tree_a.set("I002", 0, "v = {}".format(v))
    tree_b.set("I001", 0, "n = {}".format(n))
    tree_b.set("I002", 0, "v = {}".format(v))
    btn_send_close["state"] = "enabled"

def click_send_keys_close():
    tree_a.set("I003", 0, "s = {}".format(s))
    btn_z["state"] = "enabled"

def gen_z():
    global r,z
    current_time = int(time.time())
    seed = current_time % (n - 1 + 1)
    r = 1 + seed
    tree_a.set("I004", 0, "r = {}".format(r))
    z = (r*r) % n
    tree_a.set("I005", 0, "z = {}".format(z))
    btn_send_z["state"] = "enabled"

def send_z():
    tree_b.set("I003", 0, "z = {}".format(z))
    btn_b["state"] = "enabled"
    
def gen_b():
    global b
    current_time = int(time.time())
    seed = current_time % (1 - 0 + 1)
    b = 0 + seed
    tree_b.set("I004", 0, "b = {}".format(b))
    btn_send_b["state"] = "enabled"

def send_b():
    tree_a.set("I006", 0, "b = {}".format(b))
    if b == 0:
        btn_send_r["state"] = "enabled"
    else:
        btn_y["state"] = "enabled"

def send_r():
    tree_b.set("I005", 0, "r = {}".format(r))
    btn_z_b["state"] = "enabled"

def gen_y():
    global y
    y = (r*s) % n
    tree_a.set("I007", 0, "y = {}".format(y))
    btn_send_y["state"] = "enabled"

def send_y():
    tree_b.set("I006", 0, "y = {}".format(y))
    btn_y_b["state"] = "enabled"

def z_b():
    if (z == ((r*r) % n)):
        showinfo(title="Информация", message="Аутентификация прошла успешно")

def y_b():
    if (z == ((y*y*v) % n)):
        showinfo(title="Информация", message="Аутентификация прошла успешно")
    else:
        showinfo(title="Информация", message="Аутентификация прошла успешно")

window_alg = Tk()
window_alg.title("Схема аутентификации Фейге-Фиата-Шамира")
window_alg.geometry("200x150")
btn_prime = ttk.Button(text="Проверка числа на простоту", command=Prime)
btn_prime.pack(fill=X, padx=[5, 5], pady=5, side=TOP)
btn_p = ttk.Button(text="Посредник", command=Posrednik)
btn_p.pack(fill=X, padx=[5, 5], pady=5, side=TOP)
btn_A = ttk.Button(text="А", command=A)
btn_A.pack(fill=X, padx=[5, 5], pady=5, side=TOP)
btn_B = ttk.Button(text="Б", command=B)
btn_B.pack(fill=X, padx=[5, 5], pady=5, side=TOP)
window_alg.mainloop()



#window_test = Tk()
#window_test.title("Проверка чисел на простоту")
#window_test.mainloop()