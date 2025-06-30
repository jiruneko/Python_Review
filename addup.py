a = 0
for i in range(1, 11):
    a += i
print(a)

def addup(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a

print(addup(10))

def addup_other(n):
    a = (1 + n)*n/2
    return int(a)

print(addup_other(10))