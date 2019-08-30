from decimal import Decimal as Dec, getcontext as gc
from difflib import SequenceMatcher
import threading
import time
import os
#import keyboard
import multiprocessing
import curses 

import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#variables globales
teclado = 0
iter = True
final= 0

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
def guardar(n):
    archivo = open("pi.txt", 'a')
    archivo.write(n+"\n")
    archivo.close()

def pausa():
    global teclado
    global iter
    while ((iter == True) and (final<NUM_WORKERS)):
        c = getch()
        if (c == "p"):
            c = ""
            if (teclado==0):
                teclado = 1
                print("Se pausó el programa")
            #print(teclado)
            #iter = False
            #exit(0)
            else:
                print("Se despausó el programa")
                teclado = 0
  
def PI2(K):
    global teclado
    global final
    p=0
    gc().prec = 156
    start_time = time.time()
    contador=0
    iteracion=0
    for n in range(0,K+1):
        while (teclado == True):
            if contador==0:
                print("Pausado")
                contador=1
            else:
                contador=1
            #print("\n")
        A=(-1)**n
        B=factorial(6*n)
        C=(545140134*n+13591409)
        D=(factorial(3*n))
        E=(factorial(n)**3)
        F=Dec((640320))**Dec((3*n+(3/2)))
        p=(((A*B*C)/(D*E*F))+p)
        iteracion=1+iteracion
        porcentaje=(iteracion/K)*100
        print(porcentaje)
    pi=1/(12*p)
    pi = str(pi)[:154] 
    guardar(pi)
    por=similar(pi,"3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848")
    print("\nPID: %s, similitud con pi %s, Thread Name: %s, \nValor de pi: %s " % (os.getpid(),por,threading.current_thread().name,pi))
    final = final+1;

    end_time = time.time()
    print("El tiempo del thread =", end_time - start_time)
    return

#PI2(int(input("de el valor de K: ")))

threads = list()

NUM_WORKERS=int(input("Cantidad de veces a calcular pi: "))

start_time = time.time()
threads = [threading.Thread(target=PI2 , args=(int(input("de el valor de K: ")), )) for _ in range(NUM_WORKERS)]

pausar = threading.Thread(target=pausa , name='thread_pausa')
pausar.start()
[thread.start() for thread in threads]
[thread.join() for thread in threads]
pausar.join()
end_time = time.time()

print("Threads time=", end_time - start_time)

