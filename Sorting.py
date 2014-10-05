#@tiggreen

def insertionSort(lst):
	for i in range(1, len(lst)):
		j = i
		while (j > 0 and lst[j-1] > lst[j]):
			lst[j-1], lst[j] = lst[j], lst[j-1]
			j = j-1
	return lst

def binarySearchIter(data, target):
	
	if data == None:
		return False
		
	start = 0
	end = len(data) - 1
	found = False
	
	while start <= end:
		middle = (start + end)//2
		if data[middle] == target:
			found = True
			break
		elif target < data[middle]:
			end = middle - 1
		else:
			start = middle + 1
			
	return found
	

def binarySearchRec(lst, target):
	
	if lst == []:
		return False
	
	middle = len(lst) // 2 
	
	if lst[middle] == target:
		return True
	elif target > lst[middle]:
		return binarySearchRec(lst[middle+1:], target)
	else:
		return binarySearchRec(lst[:middle], target)
	


def listExperiments():
	lst = ["red", "orange", "green", "blue"]
	lst2 = lst
	lst2[1] = "purple"
	
	for i in range(len(lst)-1, -1, -1):
		# blue, green, purple, red
		print(i, lst[i])
	
	lst2 = [0]*4
	# [0, 0, 0,0]
	print(lst2)
	#["red", "purple", "green", "blue"]
	print(lst)

def main():
	arr = [1, 3, 5, 17, 23]
	print(binarySearchRec(arr, 4))


if __name__ == '__main__':
	main()