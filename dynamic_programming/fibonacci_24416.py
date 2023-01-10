# 코드1과 코드2 실행 횟수 구하기

# 재귀함수
def fib(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)


# 동적 계획법(n-2번 반복)
def fibonacci(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2

    return f[n]


n = int(input())

print(fibonacci(n), n - 2)
