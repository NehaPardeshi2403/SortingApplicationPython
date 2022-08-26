def insertion_sort(B):
    for i in range(1, len(B)):
        sorted = B[i]
        unsorted = i - 1
        while unsorted >= 0 and sorted < B[unsorted]:
            B[unsorted +1] = B[unsorted]
            unsorted = unsorted - 1
        B[unsorted+1] = sorted
        print(B)