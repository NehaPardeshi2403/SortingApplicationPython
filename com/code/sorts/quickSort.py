def pivot_element(inputArray, first, last):
    pivot = inputArray[first]
    left = first + 1
    right = last
    while True:
        while left <= right and inputArray[left] <= pivot:
            left = left + 1
        while left <= right and inputArray[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            inputArray[left], inputArray[right] = inputArray[right], inputArray[left]
    inputArray[first], inputArray[right] = inputArray[right], inputArray[first]
    return right


def quick_sort(inputArray, first, last):
    if first < last:
        p = pivot_element(inputArray, first, last)
        quick_sort(inputArray, first, p - 1)
        quick_sort(inputArray, p + 1, last)
    print(inputArray)
