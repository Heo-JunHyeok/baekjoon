def plus_cnt(n):
    cnt_list = [0, 1, 2, 4]

    for i in range(4, n + 1):
        cnt_list.append(cnt_list[i - 1] + cnt_list[i - 2] + cnt_list[i - 3])

    return cnt_list[n]


for i in range(int(input())):
    n = int(input())
    print(plus_cnt(n))
