def selective(array):
	for i in range(1,len(array)):
		index,j = array[i],i
		while(j>0 and array[j-1] > index):
			array[j] = array[j-1]
			j = j-1
		array[j] = index
		
	return array
		
	


print(selective([29, 64, 73, 34, 20]))
