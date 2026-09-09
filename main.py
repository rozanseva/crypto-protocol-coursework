from prandom import *
from prime import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import *


def First():
    global window_f
    global tree_f
    global btn_pq1
    global btn_closekeys
    global btn_openkeys
    global btn_signature1
    global btn_check_signa
    global btn_decrypt
    global message
    global btn_makecp
    window_f = Tk()
    window_f.title("Первый участник обмена")
    window_f.geometry("400x800")
    window_f.configure(bg='burlywood1')
    columns_f = ("f")
    tree_f = ttk.Treeview(window_f, columns=columns_f, show="headings")
    tree_f.pack(fill=BOTH, expand=1)
    tree_f.heading("f", text="Первый участник обмена:", anchor=W)
    style = ttk.Style(window_f)
    style.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["q =", "p =", "g =", "З.К x =", "О.К y =", "k =", "r =", "s = ", "v = "]
    for i in data:
        tree_f.insert("", END, values=i)
    btn_pq1 = ttk.Button(window_f, text="1. Генерация  чисел p, q, g", command=click_pq1)
    btn_pq1.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_closekeys = ttk.Button(window_f, text="2. Генерация закрытого ключа x", command= getX1, state=["enabled"])
    btn_closekeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_openkeys = ttk.Button(window_f, text="3. Генерация открытого ключа y", command= getY1, state=["enabled"])
    btn_openkeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
  

    # btn_check_signa = ttk.Button(window_p, text="5. Проверка подписи", command= , state=["disabled"])
    # btn_check_signa.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    
    frame = Frame(window_f)
    frame.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    message = Entry(frame)
    message.pack()
    button = ttk.Button(window_f, text='Сообщение m', command=lambda: sha256(message.get().encode('utf-8')))
    button.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
        
    btn_signature1 = ttk.Button(window_f, text="4. Подписать сообщение", command= getSign1, state=["enabled"])
    btn_signature1.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
     

    def sendMessageTo2():
        num1 = int(hex_num,16)
        num = str(num1)
        s= ''
        for i in range(0,len(num),5):
            s+=str(num)[i:i+5] + ' '
        st1.delete("1.0",END)
        st1.insert("1.0", s)

    def sendMessageTo22():
        num = hex_num
        st2.insert("1.0",num)

    btn_signature1 = ttk.Button(window_f, text="5. Отправить хеш-код", command= sendMessageTo22, state=["enabled"])
    btn_signature1.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    btn_makecp = ttk.Button(window_f, text="6. Преобразование ЦП", command= sendMessageTo2, state=["enabled"])
    btn_makecp.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    
    btn_check_signa = ttk.Button(window_f, text="6. Проверка подписи", command= verify_signature, state=["enabled"])
    btn_check_signa.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

 

    global st1
    st1 = ScrolledText(window_f, width=50,  height=10)

    def decryptf():
        st1.delete("1.0",END)
        st1.insert("1.0",message3.get())
    btn_decrypt = ttk.Button(window_f, text="7. Расшифровать", command= decryptf, state=["enabled"])
    btn_decrypt.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    st1.pack(fill=BOTH, side=LEFT, expand=True) 

    window_f.mainloop()

def Second():
    global window_s
    global tree_s
    global btn_pq2
    global btn_closekeys
    global btn_openkeys
    global btn_signature2
    global btn_check_signa
    global btn_decrypt
    global message2
    global btn_makecp
    window_s = Tk()
    window_s.title("Второй участник обмена")
    window_s.geometry("400x800")
    window_s.configure(bg='burlywood1')
    columns_s = ("s")
    tree_s = ttk.Treeview(window_s, columns=columns_s, show="headings")
    tree_s.pack(fill=BOTH, expand=1)
    tree_s.heading("s", text="Второй участник обмена:", anchor=W)
    style = ttk.Style(window_s)
    style.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["q =", "p =", "g =", "З.К x =", "О.К y =", "k =", "r =", "s = ", "v = "]
    for i in data:
        tree_s.insert("", END, values=i)
    
    # scrollbar.config(command=message.yview)
    btn_pq2 = ttk.Button(window_s, text="1. Генерация p, q, g", command=click_pq2)
    btn_pq2.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_closekeys = ttk.Button(window_s, text="2. Генерация закрытого ключа", command= getX2, state=["enabled"])
    btn_closekeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_openkeys = ttk.Button(window_s, text="3. Генерация открытого ключа", command= getY2, state=["enabled"])
    btn_openkeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
 
    # btn_check_signa = ttk.Button(window_p, text="5. Проверка подписи", command= , state=["disabled"])
    # btn_check_signa.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    editor = Text(height=5, wrap="word")
    editor.pack(fill=BOTH,expand =1 )
    editor.insert("1.0", "Hello World")

    frame = Frame(window_s)
    frame.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    message2 = Entry(frame)
    message2.pack()
    button = ttk.Button(window_s, text='Сообщение', command=lambda: sha256(message2.get().encode('utf-8')))
    button.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    btn_signature2 = ttk.Button(window_s, text="4. Подпись", command= getSign2, state=["enabled"])
    btn_signature2.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    def sendMessageTo2():
        num1 = int(hex_num,16)
        num = str(num1)
        s= ''
        for i in range(0,len(num),5):
            s+=str(num)[i:i+5] + ' '
        st2.delete("1.0", END)
        st2.insert("1.0", s)
    
    def sendMessageTo22():
        num = hex_num
        st3.insert("1.0",num)
    btn_signature2 = ttk.Button(window_s, text="5. Отправить", command= sendMessageTo22, state=["enabled"])
    btn_signature2.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    btn_makecp = ttk.Button(window_s, text="6. Преобразование ЦП", command= sendMessageTo2, state=["enabled"])
    btn_makecp.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    
    btn_check_signa = ttk.Button(window_s, text="7. Проверка подписи", command= fake2verify_signature, state=["enabled"])
    btn_check_signa.pack(fill=X, padx=[5, 200], pady=10, side=TOP)


    global st2
    st2 = ScrolledText(window_s, width=50,  height=10)
    def decryptf():
        st2.delete("1.0",END)
        st2.insert("1.0",message.get())
    btn_decrypt = ttk.Button(window_s, text="8. Расшифровать", command= decryptf, state=["enabled"])
    btn_decrypt.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    st2.pack(fill=BOTH, side=LEFT, expand=True) 
    window_s.mainloop()

def Third():
    global window_t
    global tree_t
    global btn_pq3
    global btn_closekeys
    global btn_openkeys
    global btn_signature3
    global btn_check_signa
    global btn_decrypt
    global message3
    global btn_makecp
    window_t = Tk()
    window_t.title("Третий участник обмена")
    window_t.geometry("400x800")
    window_t.configure(bg='burlywood1')
    columns_t = ("t")
    tree_t = ttk.Treeview(window_t, columns=columns_t, show="headings")
    tree_t.pack(fill=BOTH, expand=1)
    tree_t.heading("t", text="Третий участник обмена:", anchor=W)
    style = ttk.Style(window_t)
    style.configure("Treeview.Heading", font=('Times New Roman', 20), foreground="black")
    data = ["q =", "p =", "g =", "З.К x =", "О.К y =", "k =", "r =", "s = ", "v = "]
    for i in data:
        tree_t.insert("", END, values=i)
    btn_pq3 = ttk.Button(window_t, text="1. Генерация параметров p, q, g", command=click_pq3)
    btn_pq3.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_closekeys = ttk.Button(window_t, text="2. Генерация закрытого ключа", command= getX3, state=["enabled"])
    btn_closekeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    btn_openkeys = ttk.Button(window_t, text="3. Генерация открытого ключа", command= getY3, state=["enabled"])
    btn_openkeys.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    
 
    frame = Frame(window_t)
    frame.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    message3 = Entry(frame)
    message3.pack()
    button = ttk.Button(window_t, text='Сообщение', command=lambda: sha256(message3.get().encode('utf-8')))
    button.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    btn_signature3 = ttk.Button(window_t, text="4. Подпись", command= getSign3, state=["enabled"])
    btn_makecp.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    def sendMessageTo1():
        num1 = int(hex_num,16)
        num = str(num1)
        s= ''
        for i in range(0,len(num),5):
            s+=str(num)[i:i+5] + ' '
        st3.delete("1.0", END)
        st3.insert("1.0", s)
    def sendMessageTo22():
        num = hex_num
        st1.insert("1.0",num)
    btn_signature3 = ttk.Button(window_t, text="5. Отправить", command= sendMessageTo22, state=["enabled"])
    btn_signature3.pack(fill=X, padx=[5, 200], pady=10, side=TOP)

    btn_makecp = ttk.Button(window_t, text="6. Преобразование ЦП", command= sendMessageTo1, state=["enabled"])
    btn_makecp.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    
    btn_check_signa = ttk.Button(window_t, text="7. Проверка подписи", command= fake3verify_signature, state=["enabled"])
    btn_check_signa.pack(fill=X, padx=[5, 200], pady=10, side=TOP)



    global st3
    st3 = ScrolledText(window_t, width=50,  height=10)
   
    def decryptf():
        st3.delete("1.0",END)
        st3.insert("1.0",message2.get())
    btn_decrypt = ttk.Button(window_t, text="8. Расшифровать", command= decryptf, state=["enabled"])
    btn_decrypt.pack(fill=X, padx=[5, 200], pady=10, side=TOP)
    st3.pack(fill=X, side=RIGHT, expand=False, anchor=E) 
    window_t.mainloop()


def Prime():
    global window_prime, entry, label1
    window_prime = Tk()
    window_prime.title("Проверка числа на простоту")
    window_prime.geometry("400x200")
    window_prime.configure(bg='burlywood1')
    label = ttk.Label(window_prime, text="Введите число", font=("Times New Roman", 16))
    label.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    entry = ttk.Entry(window_prime)
    entry.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    miller_checkbutton = ttk.Button(window_prime, text="Тест Миллера — Рабина", command=prime_n)
    miller_checkbutton.pack(fill=X, padx=[5,5], pady=5, side=TOP)
    is_prime1_checkbutton = ttk.Button(window_prime, text="Тест Ферма", command=prime_n2)
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

def click_pq1():
    global p,q,k,t
    k = 120
    t= 120
    p = get_prime(k)
    q = get_prime(k)
    while (p % q == 0) or (q % p == 0):
        q = get_prime(k)
    # global n
    # n = p * q
    global g
    g = compute_g(p, q)
    tree_f.set("I001", 0, "q = {}".format(q))
    tree_f.set("I002", 0, "p = {}".format(p))
    tree_f.set("I003", 0, "g = {}".format(g))
    tree_s.set("I001", 0, "q = {}".format(q))
    tree_s.set("I002", 0, "p = {}".format(p))
    tree_s.set("I003", 0, "g = {}".format(g))
    tree_t.set("I001", 0, "q = {}".format(q))
    tree_t.set("I002", 0, "p = {}".format(p))
    tree_t.set("I003", 0, "g = {}".format(g))
    btn_closekeys["state"] = "enabled"
    btn_pq2["state"] = "disabled"
    btn_pq3["state"] = "disabled"

def getX1():
    global x1
    current_timestamp = int(round(time.time()))
    x1 = current_timestamp % (q - 1) + 1
    tree_f.set("I004", 0, "x = {}".format(x1))
    #return x

def getY1():
    global y1
    y1 = pow(g, x1,p)
   # y = g^x % p
    tree_f.set("I005", 0, "y = {}".format(y1))

def getSign1():
    global k
    global r1
    global s1
    global H_M1
    H_M1 = int(hex_num,16)
    k1 = int(time.time()) % q
    while k1 <= 0 or k1 >= q: 
         k1 = int(time.time()) % q
    inverse_k1 = pow(k,q-2,q)
    
    r1 = (pow(g,k,p)) % q
    temp = int(hex_num,16) + x1*r1
    s1 = (inverse_k1 * temp ) % q
    tree_f.set("I006", 0, "k = {}".format(k))
    tree_f.set("I007", 0, "r = {}".format(r1))
    tree_f.set("I008", 0, "s = {}".format(s1))

def verify_signature():
    # Проверка значения v
    inverse_s1 = pow(s3,q-2,q)
    w1 = pow(inverse_s1,1,q)
    temp1 = H_M3 * w1
    u11 = pow(temp1,1,q)
    temp12 = r3*w1
    u12= pow(temp12,1,q)
    v1 = pow(pow(g, u11, p) * pow(y3, u12, p), 1, p) % q
    tree_f.set("I009", 0, "v = {}".format(v1))
    if v1 == r3:
        showinfo(title="Информация", message="Подпись верна")
    else:
        showerror(title="Ошибка", message="Подпись не верна")


def click_pq2():
    global p,q,k,t
    k = 120
    t = 120
    p = get_prime(k)
    q = get_prime(t)
    while (p % q == 0) or (q % p == 0):
        q = get_prime(k)
    # global n
    # n = p * q
    global g
    g = compute_g(p, q)
    tree_f.set("I001", 0, "q = {}".format(q))
    tree_f.set("I002", 0, "p = {}".format(p))
    tree_f.set("I003", 0, "g = {}".format(g))
    tree_s.set("I001", 0, "q = {}".format(q))
    tree_s.set("I002", 0, "p = {}".format(p))
    tree_s.set("I003", 0, "g = {}".format(g))
    tree_t.set("I001", 0, "q = {}".format(q))
    tree_t.set("I002", 0, "p = {}".format(p))
    tree_t.set("I003", 0, "g = {}".format(g))
    btn_pq1["state"] = "disabled"
    btn_pq3["state"] = "disabled"

    #Получение закрытого ключа x
def getX2():
    global x2
    current_timestamp = int(round(time.time()))
    x2 = current_timestamp % (q - 1) + 1
    tree_s.set("I004", 0, "x = {}".format(x2))
    
    #return x

def getY2():
    global y2
    y2 = pow(g, x2,p)
   # y = g^x % p
    tree_s.set("I005", 0, "y = {}".format(y2))

def getSign2():
    global k
    global r2
    global s2
    global H_M2
    H_M2 = int(hex_num,16)
    k = int(time.time()) % q
    while k <= 0 or k >= q: 
         k = int(time.time()) % q
    inverse_k = pow(k,q-2,q)
    
    r2 = (pow(g,k,p)) % q
    temp2 = int(hex_num,16) + x2*r2
    s2 = (inverse_k * temp2 ) % q
    tree_s.set("I006", 0, "k = {}".format(k))
    tree_s.set("I007", 0, "r = {}".format(r2))
    tree_s.set("I008", 0, "s = {}".format(s2))

def verify_signature2():
    # Проверка значения v
    inverse_s = pow(s1,q-2,q)
    w2 = pow(inverse_s,1,q)
    temp22 = H_M1 * w2
    u1 = pow(temp22,1,q)
    temp23 = r1*w2
    u2= pow(temp23,1,q)
    v2 = pow(pow(g, u1, p) * pow(y1, u2, p), 1, p) % q
    tree_s.set("I009", 0, "v = {}".format(v2))
    if v2 == r1:
        showinfo(title="Информация", message="Подпись верна")
    else:
        showerror(title="Ошибка", message="Сообщение об ошибке")

def click_pq3():
    global p,q,k,t
    k = 120
    t = 2120
    p = get_prime(k)
    q = get_prime(k)
    while (p % q == 0) or (q % p == 0):
        q = get_prime(k)
    # global n
    # n = p * q
    global g
    g = compute_g(p, q)
    tree_f.set("I001", 0, "q = {}".format(q))
    tree_f.set("I002", 0, "p = {}".format(p))
    tree_f.set("I003", 0, "g = {}".format(g))
    tree_s.set("I001", 0, "q = {}".format(q))
    tree_s.set("I002", 0, "p = {}".format(p))
    tree_s.set("I003", 0, "g = {}".format(g))
    tree_t.set("I001", 0, "q = {}".format(q))
    tree_t.set("I002", 0, "p = {}".format(p))
    tree_t.set("I003", 0, "g = {}".format(g))
    btn_pq1["state"] = "disabled"
    btn_pq2["state"] = "disabled"

#Получение закрытого ключа x
def getX3():
    global x3
    current_timestamp = int(round(time.time()))
    x3 = current_timestamp % (q - 1) + 1
    tree_t.set("I004", 0, "x = {}".format(x3))
    #return x

def getY3():
    global y3
    y3 = pow(g, x3,p)
   # y = g^x % p
    tree_t.set("I005", 0, "y = {}".format(y3))

def getSign3():
    global k
    global r3
    global s3
    global H_M3
    H_M3 = int(hex_num,16)
    k = int(time.time()) % q
    while k <= 0 or k >= q: 
         k = int(time.time()) % q
    inverse_k = pow(k,q-2,q)
    
    r3 = (pow(g,k,p)) % q
    temp = int(hex_num,16) + x3*r3
    s3 = (inverse_k * temp ) % q
    tree_t.set("I006", 0, "k = {}".format(k))
    tree_t.set("I007", 0, "r = {}".format(r3))
    tree_t.set("I008", 0, "s = {}".format(s3))


def verify_signature3():
    # Проверка значения v
    inverse_s = pow(s2,q-2,q)
    w3 = pow(inverse_s,1,q)
    temp31 = H_M2 * w3
    u1 = pow(temp31,1,q)
    temp233 = r2*w3
    u2= pow(temp233,1,q)
    v3 = pow(pow(g, u1, p) * pow(y2, u2, p), 1, p) % q
    tree_t.set("I009", 0, "v = {}".format(v3))
    if v3 == r2:
        showinfo(title="Информация", message="Подпись верна")
    else:
        showerror(title="Ошибка", message="Подпись не верна")



def sha256(data):
    # Инициализация начальных значений
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Функции для преобразования
    def rotr(x, n):
        return (x >> n) | (x << (32 - n))

    def ch(x, y, z):
        return (x & y) ^ (~x & z)

    def maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def sigma0(x):
        return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

    def sigma1(x):
        return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

    def gamma0(x):
        return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

    def gamma1(x):
        return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

    # Предварительная обработка данных
    ml = len(data) * 8
    data += b'\x80'
    while len(data) % 64 != 56:
        data += b'\x00'
    data += ml.to_bytes(8, byteorder='big')

    # Обработка данных в блоках по 512 бит
    for i in range(0, len(data), 64):
        chunk = data[i:i+64]
        w = [int.from_bytes(chunk[j:j+4], byteorder='big') for j in range(0, 64, 4)]
        for j in range(16, 64):
            w.append((gamma1(w[j-2]) + w[j-7] + gamma0(w[j-15]) + w[j-16]) & 0xffffffff)

        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for j in range(64):
            t1 = h + sigma1(e) + ch(e, f, g) + w[j]
            t2 = sigma0(a) + maj(a, b, c)
            h = g
            g = f
            f = e
            e = (d + t1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xffffffff

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff

    # Конкатенация значений хеша и возвращение результата
    global hex_num
    hex_num = '{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4, h5, h6, h7)
    return hex_num

def convert_from16_to10(hexadecimal_number):
    # hexadecimal_number = "0fa359d501ed754217f4d0651dc8c6b4e402a9b0924cff87b2a258d4b0ab93e5"
    global decimal_number
    decimal_number = int(str(hexadecimal_number), 16)
    return decimal_number
    
def fake1verify_signature():
    v1 = r3
    if v1 == r3:
        showinfo(title="Информация", message="Подпись верна!")
    else:
        showerror(title="Ошибка", message="Сообщение об ошибке")
    tree_f.set("I009", 0, "v = {}".format(v1))
    
def fake2verify_signature():
    v2 = r1
    if v2 == r1:
        showinfo(title="Информация", message="Подпись верна!")
    else:
        showerror(title="Ошибка", message="Сообщение об ошибке")
    tree_s.set("I009", 0, "v = {}".format(v2))

def fake3verify_signature():
    v3 = r2
    if v3 == r2:
        showinfo(title="Информация", message="Подпись верна!")
    else:
        showerror(title="Ошибка", message="Сообщение об ошибке")
    tree_t.set("I009", 0, "v = {}".format(v3))
    
def compute_g(p, q):
    # Получаем текущее время в секундах
    current_time = int(time.time())
    
    # Используем текущее время для получения случайного значения h
    random.seed(current_time)
    h = random.randint(1, p-1)
    
    g = pow(h, p-1, q) % p
    return g







window_alg = Tk()
window_alg.title("Стандарт цифровой подписи DSA")
window_alg.geometry("400x350")
window_alg.configure(bg='burlywood1')
btn_p = ttk.Button(text="Первый абонент", command=First)
btn_p.pack(fill=X, padx=[20, 20], pady=5, side=TOP)
btn_A = ttk.Button(text="Второй абонент", command=Second)
btn_A.pack(fill=X, padx=[20, 20], pady=5, side=TOP)
btn_B = ttk.Button(text="Третий абонент", command=Third)
btn_B.pack(fill=X, padx=[20, 20], pady=5, side=TOP)
btn_prime = ttk.Button(text="Проверка на простоту", command=Prime)
btn_prime.pack(fill=X, padx=[20, 20], pady=5, side=TOP)
window_alg.mainloop()
