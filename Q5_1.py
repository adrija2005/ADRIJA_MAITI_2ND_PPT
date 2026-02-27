arr = [10, 20, 30, 40, 50]
sum_even_idx = sum(arr[i] for i in range(0, len(arr), 2))
print(sum_even_idx)