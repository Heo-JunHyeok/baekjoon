# 방법 1 : 구현
# import sys

# for _ in range(int(sys.stdin.readline())):
#     vps = sys.stdin.readline().strip()

#     if vps.count("(") != vps.count(")"):
#         print("NO")
#         continue

#     while "()" in vps:
#         vps = vps.replace("()", "")

#     if len(vps) != 0:
#         print("NO")
#     else:
#         print("YES")

# 방법 2 : 스택
import sys


def stack(valid_ps):
    result = []

    if valid_ps.count("(") != valid_ps.count(")"):
        return "NO"

    for i in valid_ps:
        if i == ")":
            if len(result) == 0:
                return "NO"
            result.pop()
        elif i == "(":
            result.append(")")

    return "YES"


for _ in range(int(sys.stdin.readline())):
    vps = sys.stdin.readline().strip()

    print(stack(vps))
