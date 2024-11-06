a = 0
for i in range(1,10,1):
    if i % 2 == 0:              # i % 2 != 0: เลขคู่      i % 2 == 0: เลขคี่
        continue
    print(i)