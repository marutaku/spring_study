array = [9, 6, 7, 1, 2]
  #配列の順番を決める
for i in range(1, len(array)):
    for j in range(i):
        if array[i] < array[j]:
            array[j], array[i] = array[i], array[j]
        print(array)