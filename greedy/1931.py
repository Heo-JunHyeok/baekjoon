meeting_time = []

for _ in range(int(input())):
    meeting_time.append(list(map(int, input().split())))

meeting_time.sort(key=lambda x: (x[1], x[0]))

end_time = 0
result = 0

for start, end in meeting_time:
    if start >= end_time:
        result += 1
        end_time = end

print(result)
