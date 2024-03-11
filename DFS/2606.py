def dfs(n):

    stack.append(n)
    visited[n] = True

    while stack:
        node = stack.pop()
        for i in linked_node[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    return visited.count(True)


c = int(input())
num = int(input())
linked_node = [[] for _ in range(c + 1)]
stack = []
visited = [False for _ in range(c + 1)]
# node, visited: 1번 컴퓨터부터 시작, 0번 인덱스 사용 x

for i in range(num):
    l, r = map(int, input().split())
    linked_node[l].append(r)
    linked_node[r].append(l)
    """
        [1,2,5],[2,1,3,5],[3,2],[4,7],[5,1,2,6],[6,5],[7,4]
        반복문을 통해 이어져 있는 노드에 접근하기 위해
    """

print(dfs(1) - 1)  # 1번 컴퓨터는 결과에 포함 x
