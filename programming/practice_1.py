from collections import defaultdict
from random import choice


c = float(input())

print(c, "по Цельсию =", f"{(c*9/5)+32:.2f}", "по Фаренгейту")
print(c, "по Цельсию =", f"{c+273.15:.2f}", "по Кельвину")


n = int(c)

if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
if n > 0:
    print("+")
elif n == 0:
    print(0)
else:
    print("-")
if 10 <= n <= 50:
    print("Yes")
else:
    print("No")


a = "AQWERTYUIOPSDFGHJKLZXCVBNM"
num = "1234567890"
s = "!@#$%^&*"
k = l = p = ""

for i in range(3):
    k += choice(a)
    l += choice(num)
for i in range(2):
    p += choice(s)
print(k, l, p)


a = input().lower()
kp = defaultdict(int)
for i in a:
    kp[i] += 1
print(sorted(kp.items())[:3])


n = int(input())
p = [i for i in range(n + 1)]
p[1] = 0
i = 2
while i <= n:
    if p[i] != 0:
        j = i + i
        while j <= n:
            p[j] = 0
            j += i
    i += 1
p = [i for i in p if i != 0]
print(p)


i = 1234567890
l = 1
c = 9
while i > l * c:
    i -= l * c
    l += 1
    c *= 10
n = 10**(l - 1) + (i - 1) // l
di = (i - 1) % l
print(str(n)[di])

