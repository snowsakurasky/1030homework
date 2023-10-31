n = int(input('請輸入星星數量:'))
s = (n + 1) // 2
for a in range(1, s+1):
    for nu in range(s-a):
        print(" ", end="")
    for star in range(1+(a-1)*2):
        print("*", end="")
    print()
for b in range(s-1, 0, -1):
    for nu in range(s-b, 0, -1):
        print(" ", end="")
    for star in range(2*b-1):
        print("*", end="")
    print()
