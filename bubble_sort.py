def change (count,array):
    tmp=array[count]
    array[count] , array[count+1] = array[count+1] , array[count]
    return array

array = [9,6,7,1,2]

print(len(array))

for i in range (len(array) - 2):
    
    for j in range (len(array) - 1 - i):
        if array[j] > array[j + 1]:
            change(j,array)
        print(array)
        

