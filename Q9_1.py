arr = [1, 2, 3, 4, 5]
arr.remove(max(arr))
arr.remove(min(arr))
avg = sum(arr) / len(arr)
print(int(avg))