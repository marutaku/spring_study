#fvnc.py
def sumfvnc(fvnc):
    number = fvnc[-1] + fvnc[-2]
    return number


number = int(input())
fvnc = []
i = 0
for i in range(number):
    if i <= 1:
        fvnc.append(i)
    else:
        fvnc.append(sumfvnc(fvnc))
    i += 1
print(fvnc)


