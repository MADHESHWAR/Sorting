n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted List : \n",arr)
