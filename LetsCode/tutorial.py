def fib_iter(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        c = a + b
        a = b
        b = c
    return a

def fib_rec(n):  
   if n <= 1:  
       return n  
   else:  
       return fib_rec(n-1) + fib_rec(n-2)

def fib_dyn(n):                                                                                                 
    seq = np.zeros(n+1)
    seq[0] = 0
    seq[1] = 1
    for i in range(2, n+1):
        seq[i] = seq[i-1] + seq[i-2]
        print(seq[i])
    return seq[n]


#recurssion BFS, minmax