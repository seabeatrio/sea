y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
if x1 + 1 == x2 or y1 + 1 == y2:
    print('NO')
elif x2 + 1 == x1 or y2 + 1 == y1:
    print('NO')
elif x1 + 1 >= x2 and y1 + 1 <= y2:
    print('YES')
elif x1 + 1 >= x2 and y2 + 1 <= y1:
    print('YES')
elif x2 + 1 >= x1 and y1 + 1 <= y2:
    print('YES')
elif x2 + 1 >= x1 and y2 + 1 <= y1:
    print('YES')
else:
    print('NO')