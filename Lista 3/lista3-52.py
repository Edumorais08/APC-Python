def is_palindrome(s):
    return s == s[::-1]

s = input()
conta = 0

for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        conta += 1

if conta == 1 or (conta == 0 and len(s) % 2 == 1):
    print("ON")
else:
    print("OFF")
