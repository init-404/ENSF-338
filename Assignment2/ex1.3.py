def func(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = func(n-1, memo) + func(n-2, memo)
    return memo[n]
