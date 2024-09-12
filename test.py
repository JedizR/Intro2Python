def fibo(n,memo : list):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2 :
        result = 1
    else:
        result = fibo(n-1, memo) + fibo(n-2, memo)
    memo[n] = result
    return result
mem = {}
fibo(1000,mem)
print(mem)

