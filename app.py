from audioop import reverse


def find_max(numbers):
    highest = max(numbers)
    return highest
    
array_one = [44,66,77,3444,555,7673,32434]
print(find_max(array_one))

def second_largest(numbers):
    numbers.sort(reverse = True)
    return numbers[1]

print(second_largest(array_one))

def k_largest(numbers,index):
    numbers.sort(reverse = True)
    k = index - 1
    return numbers[k] 

print(array_one)
print(k_largest(array_one,3))