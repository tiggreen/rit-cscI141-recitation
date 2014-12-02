# Author @tigranhk
# Fast sorting algorithms: Merge and Quick sorts.

def mergeSort(lst):
    if not lst:
        return lst
    elif (len(lst) == 1):
        return lst
    else:
        (half1, half2) = split(lst)
        return merge(mergeSort(half1), mergeSort(half2))

# Split the list into two chunks.
def split(lst):
    evens = []
    odds = []
    isEven = True
    for e in lst:
        if isEven:
            evens.append(e)
        else:
            odds.append(e)
        isEven = not isEven
    return ( evens, odds )

# Merge two sorted lists into one.
def merge(sorted1, sorted2):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if ( sorted1[index1] <= sorted2[index2]):
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1

    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])

    return result

# Quick sort.
def quickSort(lst):
    if not lst:
        return lst
    else:
        # Not a good idea.
        pivot = lst[0]
        (less, same, more) = partition(pivot, lst)
        return quickSort(less) + same + quickSort(more)


def partition(pivot, lst):
    (less, same, more) = ([],[],[])
    for e in lst:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def main():
    a = [1, 5, 55, 7, 10, 8, 0, 3, 1, 2, 2, 0, 12, 33, 18]
    b = [1, 6, 3, 4, 12, 55, 33, 33, 44, 17, 16]
    print ("QuickSort result: " + str(quickSort(a)))
    print ("MergeSort result: " + str(mergeSort(b)))


main()
