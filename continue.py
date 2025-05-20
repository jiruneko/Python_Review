for i in range(0,10):
    print('こんにちは')
    
total = 0
for j in range(100):
    if j % 3 == 0:
        continue
    print(j)
    total += j
    
print('合計は', total)
