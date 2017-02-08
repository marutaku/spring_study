array = [9,6,7,1,2]
for i in range(len(array)+1):
	for j in array:
		if j < array[i]:
			array[i] = array[i]
			array[i]=j
print(array)
