s = input()
t = s
v = s
w = s
x = s

for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        s = s.replace(i,'a')

print(s)

for i in t:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        t = t.replace(i,'e')

print(t)

for i in v:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v = v.replace(i,'i')

print(v)

for i in w:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        w = w.replace(i,'o')

print(w)

for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        x = x.replace(i,'u')

print(x)