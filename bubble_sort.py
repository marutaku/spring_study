def change (count,array):
	tmp=array[count]
	array[count]=array[count+1]
	array[count+1]=tmp
	return array

array = [9,6,7,1,2]

i=0

while i<len(array):
	count=0
	while count<=(len(array)-2):
		if array[count]>array[count+1]:
			change(count,array)
		count=count+1
		pass
	i=i+1
	pass
print(array)
