array = [9,6,7,1,2]
sort_array = []
for i in range(len(array)): #配列の順番を決める
    sort_array.append(array.pop(0))
    for j in range(len(sort_array)):
        if sort_array[- 1] < sort_array[j]:
            sort_array[j], sort_array[i] = sort_array[i], sort_array[j]
        print(sort_array)
