arr = [1, 2, 4, 3, 5, 6]
max_so_far = arr[0]
result = None

for i in range(1, len(arr)):
    if arr[i] > max_so_far:
        result = arr[i]
        break
    else:
        max_so_far = max(max_so_far, arr[i])

if result is not None:
    print(result)
else:
    print("No such element")