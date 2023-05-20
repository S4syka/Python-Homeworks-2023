def sum_no_duplicates(l):
    return sum(number for number in l if l.count(number) == 1)

print(sum_no_duplicates([3,4,3,6]))