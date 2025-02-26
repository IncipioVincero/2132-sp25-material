def bin_search_rec(arr, x)

  if len(arr) == 0: 
    return False

  mid = len(arr) // 2
  if arr[mid] > x: 
    return bin_search_rec(arr[:mid],x)
  elif arr[mid] < x:
    return bin_search_rec(arr[mid+1:],x)
  else:  # arr[mid] == x
    return True



def binary_search(arr, x): 
  left = 0
  right = len(arr)-1

  mid = (left + right) // 2
  while left<=right and arr[mid] != x: 

      print("index", mid,":", arr[mid])
      if arr[mid] > x: # x must be located in the first half
        right = mid - 1

      elif arr[mid] < x: # x must be located in second half 
        left = mid + 1

      mid = (left + right) // 2

  print("index", mid,":", arr[mid])
  if left <= right: 
    return mid
  else: 
    -1   

if __name__ == "__main__":

  li = [1, 7, 13, 23, 42, 55, 100]

  x = 55 
  index = binary_search(li, x)

  print("Found",x,"at index",index)
