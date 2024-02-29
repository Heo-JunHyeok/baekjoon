import itertools

a, b = map(list, input().split())
result = -1

for permutation in itertools.permutations(a, len(a)):
    if permutation[0] != "0":
        int_per = int("".join(permutation))
        if int_per < int("".join(b)):
            result = max(result, int_per)

print(result)
