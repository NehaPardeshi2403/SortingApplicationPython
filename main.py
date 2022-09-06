import com.code.sorts.bubbleSort as bubbleSort
import com.code.sorts.selectionSort as selectionSort
import com.code.sorts.insertionSort as insertionSort
import com.code.sorts.quickSort as quickSort

A = [3, 4, 9, 10, 3, 2, 120]
# TODO for Development Branch
def sorting_algorithum():
    userInput = int(input("For Bubble Sort Enter : 1 \n"
                          "For Selection Sort Enter : 2 \n"
                          "For Insertion Sort Enter : 3 \n"
                          "For Quick Sort: 4 \n"
                          "For Nothing  Enter : 5  : \n"
                          "Enter the sorting method: "))

    if userInput == 1:
        print("Using Bubble Sort")
        bubbleSort.bubble_sort(A)
    elif userInput == 2:
        print("Using Selection  Sort")
        selectionSort.selection_sort(A)
    elif userInput == 3:
        print("Using Insertion Sort")
        insertionSort.insertion_sort(A)
    elif userInput == 4:
        print("Using Quick Sort")
        quickSort.quick_sort(A, 0, len(A) - 1)
    else:
        print("there is no another sorting method")


sorting_algorithum()
# Added new function.

def again():
    r = input("Would you like to restart this program?")
    if r == "yes" or r == "y":
        return sorting_algorithum()
    elif r == "n" or r == "no":
        print("See you in the next one. Goodbye.")

again()
