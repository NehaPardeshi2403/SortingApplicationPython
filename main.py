import com.code.sorts.bubbleSort as bubbleSort
import com.code.sorts.selectionSort as selectionSort
import com.code.sorts.insertionSort as insertionSort
#import com.code.sorts.quickSort as quickSort
A = [3, 4, 9, 10, 3, 2, 120]
bubble = "bubbleSort"
selection = "selectionSort"
insertion = "insertionSort"
userInput = input("Enter the sorting method: ")

if bubble == userInput:
    print("Using Bubble Sort")
    bubbleSort.bubble_sort(A)
elif selection == userInput:
    print("Using Selection  Sort")
    selectionSort.selection_sort(A)
elif insertion == userInput:
    print("Using Insertion Sort")
    insertionSort.insertion_sort(A)
else:
    print("there is no another sorting method")

