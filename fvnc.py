#fvnc.py
def sumfvnc(fvnc,count):
	sum=0
	i=0
	while i <= 1:
		sum+=fvnc[count-i]
		i+=1
	return sum




number=int(input())
fvnc=[]
i=0
while i<(number):
	if i<=1:
		fvnc.append(i)
	else:
		fvnc.append(sumfvnc(fvnc,i-1))
	i+=1
	pass
print(fvnc)


