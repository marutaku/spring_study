#fvnc.py
def sumfvnc(fvnc):
    return = fvnc[-1] + fvnc[-2]
    

number = int(input())
fvnc = []
for i in range(number):
    if i <= 1:
        fvnc.append(i)
    else:
        fvnc.append(sumfvnc(fvnc))
print(fvnc)


