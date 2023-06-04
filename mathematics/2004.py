import sys

n, m = map(int, sys.stdin.readline().split())
n_power = [0, 0]
m_power = [0, 0]
square_5 = 5
square_2 = 2

while square_5 <= n:
    n_power[0] += n // square_5
    m_power[0] += (m // square_5) + ((n - m) // square_5)
    square_5 *= 5

while square_2 <= n:
    n_power[1] += n // square_2
    m_power[1] += (m // square_2) + ((n - m) // square_2)
    square_2 *= 2


print(min(n_power[0] - m_power[0], n_power[1] - m_power[1]))
