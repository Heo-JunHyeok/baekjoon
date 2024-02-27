a, b, c, x, y = map(int, input().strip().split())

two_c = 2 * c

axby=a*x+b*y

two_c_max=two_c*max(x,y)

ab_two_c=(x-y)*a+y*two_c if x>=y else (y-x)*b+x*two_c

result=min(axby, two_c_max, ab_two_c)

print(result)