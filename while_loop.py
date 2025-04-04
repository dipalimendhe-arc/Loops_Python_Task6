# 1. While loop with division

num = 100
while num > 1:
    num = num/2
    print(num)

# 2. Updating dictionary values in a loop

D1 = {'x': 10, 'y': 20, 'z': 30}
while D1['x'] < 50:
    D1['x'] += 5
print(D1)

# 3. Iterating until a key is found

D2 = {'apple': 1, 'banana': 2, 'cherry': 3}

key_to_find = 'banana'

key_found = False
while not key_found:
    
    for key in D2.keys():
        if key == key_to_find:
            print("Key found:", key)
            key_found = True

# 4.Iterating through a list

L1 = [2, 4, 6, 8, 10]
i = 0
while i < len(L1):
    print(L1[i])
    i += 1

# 5. Filtering even numbers in a loop

numbers = [1, 3, 4, 6, 7, 8]
filtered_list = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        filtered_list.append(numbers[i])
    i += 1
print(filtered_list)

# 6. Creating a list of square of elements in a loop

def square(x):
    return x * x

n = 1
squares = []
while n <= 5:
    squares.append(square(n))
    n += 1
print(squares)

# 7. Checking conditions in a while loop

num = 10
while num > 0:
    print("Countdown:", num)
    num = num - 1

# 8. Using a function in a loop

def even(num):
    return num % 2 == 0

num = 3
while even(num):
    num = num+1
print("Odd number:", num)


# 9. Using break with a condition

def stop_loop(val):
    return val > 50

i = 10
while True:
    if stop_loop(i):
        break
    print(i)
    i += 5

# 10. Loop with multiple lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
i = 0
while i < len(list1):
    print(list1[i] + list2[i])
    i += 1




