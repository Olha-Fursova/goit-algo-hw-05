def binary_fraction_search(arr, x):
  low = 0
  high = len(arr) - 1
  count = 0

  while low <= high:
    
    mid = (high + low) // 2
    count += 1
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    
    else:
      return mid
    
  if low < len(arr):
      upper_bound = arr[low]
      return (count, upper_bound)
  else:
      return (count, None)

result1 = binary_fraction_search([1.1, 2.3, 3.5, 4.8, 5.9, 7.0], 4.0)

result2 = binary_fraction_search([1.1, 2.3, 3.5, 4.8, 5.9, 7.0], 7.5)

print(result1)
print(result2)