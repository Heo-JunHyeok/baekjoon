import sys

k, n = map(int, input().split())
lan_list = [int(sys.stdin.readline().strip()) for _ in range(k)]
left, right = 1, max(lan_list)


def binary_search(lan_list, left, right, n):
    mid = (left + right) // 2
    
    if left > right:
        return mid

    lan_cnt = 0
    for i in lan_list:
        lan_cnt += i // mid

    if lan_cnt >= n:
        return binary_search(lan_list, mid + 1, right, n)
    else:
        return binary_search(lan_list, left, mid - 1, n)


print(binary_search(lan_list, left, right, n))
