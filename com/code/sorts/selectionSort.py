def selection_sort(A):
    for i in range(0, len(A)-1):
        for j in range(i, len(A)-1):
            if A[i] > A[j+1]:
                A[i], A[j+1] = A[j+1], A[i]

    print(A)
