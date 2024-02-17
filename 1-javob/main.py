def fibonacci(n):
    fib = [0, 1] 
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

N = int(input("Fibonachi sonlarini qaysi darajada chiqarishni xohlaysiz? "))
print(N, "ta Fibonachi sonlari:", fibonacci(N))
