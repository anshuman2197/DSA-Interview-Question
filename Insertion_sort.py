def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j =i-1
        while j >=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i],end="")
    # print()

arr=[13,46,24,52,20,9]
insertion_sort(arr)
print(arr)