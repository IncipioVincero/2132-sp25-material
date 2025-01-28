def find(arr, x):

  for i in range(len(arr)):
    print("index",i,":",arr[i])
    if arr[i] == x:
      return i

  return -1 

# Binary Search 
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
