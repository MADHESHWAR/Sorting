def selection_sort(n, arr):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)
    
print("Array before Sorting:")
for i in arr:
    print(i,end=" ")
    
selection_sort(n, arr)
    
print("\nArray after Sorting in Ascending Order:")
for i in arr:
    print(i,end=" ")
