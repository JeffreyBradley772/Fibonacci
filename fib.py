'''
Author: Jeffrey Bradley and Will Medick
Project #12
FileName: fib.py

Description:
This program calculates the nth fibonacci number with various efficiencies.
'''



import time

def fib(n):
    if n==0:
        return 0
    elif n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def faster_fib(n):
    list1 = [0,1]
    for i in range(n-1):
        newfib = list1[0] + list1[1]
        list1[0] = list1[1]
        list1 = [list1[1],newfib]
    return newfib

def timeFasterFib(n):
    t1 = time.perf_counter()
    x = faster_fib(n)
    t2 = time.perf_counter()
    print("Fib",n,"was",x)
    print("Took",t2-t1,'time.')
    
        
def timeFib(n=10):
    t1 = time.perf_counter()
    x = fib(n)
    t2 = time.perf_counter()
    print("Fib",n,"was",x)
    print("Took", t2-t1, "time")

def quick_fib(n):
    if n == 0:
        return 0,1
    else:
        a,b = quick_fib(n//2)
        x = a * (2*b - a)
        y = a**2 + b**2
        if n%2 == 0:
            return x,y
        else:
            z = x+y
            return y,z

def timeQuickFib(n):
    t1 = time.perf_counter()
    x,y = quick_fib(n)
    t2 = time.perf_counter()
    print("Fib",n,"was",x)
    print("Took", t2-t1,"time")
        
    
    
def main():
    #print(fib(20))
    #timeFib(20)
    #timeFasterFib(89)
    #timeQuickFib(89)
    
if __name__ == "__main__":
    main()
