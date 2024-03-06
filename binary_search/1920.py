n = input()
a = sorted(map(int, input().split()))
m = int(input())
number = list(map(int, input().split()))


def binary_search(a_list, number, start, end):
    
    if a_list[start] <= number <= a_list[end]:    
        mid=(start + end) // 2
        if a_list[mid] == number:
            return 1
        else:
            if a_list[mid] > number:
                return binary_search(a_list, number, start, mid)
            else:
                return binary_search(a_list, number, mid+1, end)
    else:
        return 0

start,end=0, len(a)-1
for i in number:
    print(binary_search(a, i, start,end))
