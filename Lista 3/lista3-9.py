n = int(input())
din_total = []
while n > 0:
    a = int(input())
    din_add = 0
    if a < 1000:
        din_add = 1000 - a
    din_total.append(din_add)
    n -= 1

print(sum(din_total))