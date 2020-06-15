def fat(n):
    if n == 1:
        return n
    else:
        return n * fat(n-1)

def tail_fat(n, acc=1):
    if n == 1:
        return acc
    else:
        return tail_fat(n-1, acc * n)
