def print_duplicates3(li):

  sorted_li = sorted(li)

  i = 1
  while i < len(li):
    if li[i] == li[i-1]:  # found a duplicate
      print(li[i])

      # skip all other copies of the duplicate
      while i < len(li)-1 and  li[i] == li[i+1]:
        i += 1
      
    i += 1



def print_duplicates4(li): 

  seen = set()
  duplicates = set()
  for i in li: 
    if li[i] in seen(): 
      if not li[i] in duplicates: 
        duplicates.add(li[i])
        print(li[i])
    seen.add(li[i]) 
