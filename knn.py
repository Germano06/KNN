from math import sqrt


k = int(input("Enter the k value: "))
x = int(input("Enter the testing data\nx: "))
y = int(input("y: "))
d1 = list(input("Enter dataset 1: ").split())
d2 = list(input("Enter dataset 2: ").split())
target = list(
    input("Enter data for target class (t for true, f for false): ").split()
)
s = len(d1)
d = []
cT, cF = 0, 0
for i in range(s):
    dx = int(d1[i])-x
    dy = int(d2[i])-y
    d.append(sqrt(pow(dx, 2)+pow(dy, 2)))
for i in range(s-1):
    min, l = d[i], i
    for j in range(i+1, s):
        if min > d[j]:
            min, l = d[j], j
    d[i], d[l] = d[l], d[i]
    target[i], target[l] = target[l], target[i]

for i in range(k):
    print(d[i], "->", target[i])
    if target[i] == 't':
        cT += 1
    else:
        cF += 1

if cT > cF:
    print("Target class is True")
else:
    print("Target class is False")
