#missing number in an array

def missing_num(arr,n):
    print()
    print(f'initial array {arr} with lenght {n}')
    print()
    actual_sum=0
    total_sum = n*(n+1) // 2
    print(f'total sum of n natural numbers : {total_sum}')
    for num in arr:
        actual_sum+=num
    print(f'sum of array (excluding missing number) : {actual_sum}')
    print()
    missing_num=total_sum - actual_sum
    print(f'missing number in array  : {missing_num}')
    return missing_num

#test cases
#test 1 : normal case
missing_num([1,2,3,4,5,6],6)
#test 2 : missing first element
missing_num([2,3,4,5] , 5)
#test 3 : missing last element
missing_num([1,2,3,4] , 5)
#test 4 : random missing 
missing_num([3,5,7,1,2,8,4] , 8)
#test 5 : empty array
missing_num([],1)

########### DONE   WITH EASY LEVEL TOTAL NO.OF QUES = 11