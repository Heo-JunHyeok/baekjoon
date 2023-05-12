import sys

for _ in range(int(sys.stdin.readline())):
    vps = sys.stdin.readline().strip()

    if vps.count("(") != vps.count(")"):
        print("NO")
        continue

    while "()" in vps:
        vps = vps.replace("()", "")

    if len(vps) != 0:
        print("NO")
    else:
        print("YES")
