import itertools

# 숫자 야구에 사용할 수 있는 모든 경우의 수
baseball_list = list(itertools.permutations([i for i in range(1, 10)], 3))

for _ in range(int(input())):
    number, strike, ball = map(int, input().split())
    number = list(map(int, str(number)))        # int로 입력받은 숫자를 자릿수마다 나눠서 리스트에 저장
    temp = list()

    for baseball in baseball_list:
        s_cnt, b_cnt = 0, 0
        for i in range(3):
            if number[i] in baseball:
                if number[i] == baseball[i]:
                    s_cnt += 1
                else:
                    b_cnt += 1

        if strike == s_cnt and ball == b_cnt:
            temp.append(baseball)

    baseball_list = temp


print(len(baseball_list))
