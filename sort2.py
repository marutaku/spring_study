array=[9,6,7,1,2]
i=0

while i < len(array):#配列の順番を決める
	j=0
	while j < i:#前の配列と比べる
		if array[i]<array[j]:
			tmp=array[j]
			array[j]=array[i]
			array[i]=tmp
		j=j+1
		print(array)
		pass
	i=i+1
	pass