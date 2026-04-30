#largest and second largest of array 

def largest_sec(arr):
  first=second=float('-inf')
  print(f'checking array : {arr}')
  
  for num in arr:
    if num>first:
      second=first
      first=num
    elif num>second and num!=first :
        second=num
  print(f'largest : {first} \nsecond largest : {second}')
  return first,second

arr=[3,3,13,7,9,4]
largest_sec(arr)
