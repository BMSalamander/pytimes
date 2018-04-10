import math
import random
import sympy
import time
import threading
TIME_LIMIT = 0

def GetPolynomResult(f,x):
    res = 0
    for i in range(len(f)-1):
        res += x**i * f[i]

    return res

def RoMethod(N, T, f, x0):
   # if (time.time() - TIME_LIMIT > 300):
     #   return 0
    x = [x0]
    chI = 0
    for i in range(1, T):
       # if (time.time() - TIME_LIMIT > 300):
       #     return 0
        x.append(GetPolynomResult(f, x[i-1]))
        chI = i
        k = 0
        while(chI != 0):
            chI = chI >> 1
            k += k

        k -= k
        k = 2**k - 1
        d = math.gcd(abs(x[i] - x[k]), N)

        if(d == 1):
            if (i == T - 1):
                return -1
            continue
        if (d > 1 and d < N):
            return d
        if (d == N):
            return 0
        


    return 0

def RoMethodSphere(N,e):
    #if (time.time() - TIME_LIMIT > 300):
    #    return 0
    if (sympy.isprime(N)):
        return 0
    T1 = 4 * math.trunc((math.sqrt(2*math.sqrt(N)*math.log1p(1/e))))

    a = random.randrange(1,N) # f(x)=x^2 + ax + b)
    b = random.randrange(1,N)
    f = [b, a, 1]
    x0 = random.randrange(1,N)
    counter = 0

    while(True):
        #if (time.time() - TIME_LIMIT > 300):
         #   return 0

        res = RoMethod(N, T1, f, x0)
        if (res == 0):
            counter += 1
            x0 = random.randrange(1,N)
            if (counter == N):
                 a = random.randrange(1,N)
                 b = random.randrange(1,N)
                 f = [b, a, 1]
                 counter = 0
            continue
        if (res > 0):
            return res
        if (res < 0):
            return 0
    return 0

def listmerge(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all

def Factorize_env(N):
    #if (time.time() - TIME_LIMIT > 300):
    #    return [0]
    
    Num = N
    mults = []

    while not sympy.isprime(Num):
        #if (time.time() - TIME_LIMIT > 300):
         #   return [0]
        d = RoMethodSphere(Num, 0.5)
        multsTmp = Factorize_env(d)
        Num = Num // d
        mults.extend(multsTmp)

    mults.append(Num)
    return mults

def Factorize(N):
    #if (time.time() - TIME_LIMIT > 300):
    #    return [(0,0)]
    mults = Factorize_env(N)
    newMults = []
    newPows = []

    for mult in mults:
        if (mult not in newMults):
            newMults.append(mult)
            newPows.append(mults.count(mult))
    factor = []
    for i in range(len(newMults)):
        factor.append((newMults[i],newPows[i]))

    return factor

def main():
    N = input()
    N = int(N)
    #TIME_LIMIT = time.time()
    d = RoMethodSphere(N, 0.5)
    if (d != 0):
        print(d)
    else:
        print(N,"is prime")

    myFactor = Factorize_env(N)
    print(myFactor)

    myFactor1 = Factorize(N)
    print(myFactor1)


main()
