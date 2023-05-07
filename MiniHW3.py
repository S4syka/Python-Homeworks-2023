def sum_no_duplicates(l):
    return sum({numbers for numbers in l})

print(sum_no_duplicates([1,2,3,4,5,5,5,5]))