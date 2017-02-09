array = [9,6,7,1,2]
count=0

def change (count,array):
	tmp=array[count]
	array[count]=array[count+1]
	array[count+1]=tmp
	return array

while count<=(len(array)-2):
	if array[count]>array[count+1]:
		change(count,array)
	count=count+1
	print(array)
	pass
		
