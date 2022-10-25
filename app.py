from audioop import reverse


def find_max(numbers):
    highest = max(numbers)
    return highest
    
array_one = [1000,2000,3000,4000,5000,4500,3500,2500,1500,500,0]
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
print(k_largest(array_one,11))