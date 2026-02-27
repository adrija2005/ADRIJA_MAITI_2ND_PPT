arr = [1, 2, 3, 5]
is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
print(is_sorted)