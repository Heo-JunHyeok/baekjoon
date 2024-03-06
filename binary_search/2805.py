import sys

n, m = map(int, input().split())
h_list = list(map(int, sys.stdin.readline().strip().split()))
left, right = 0, max(h_list)


def binary_search(h_list, left, right, m):
    mid = (left + right) // 2

    if left > right:
        return mid

    m_len = 0
    for i in h_list:
        if i > mid:
            m_len += i - mid

    if m_len >= m:
        return binary_search(h_list, mid + 1, right, m)
    else:
        return binary_search(h_list, left, mid - 1, m)


print(binary_search(h_list, left, right, m))
